# import pymupdf
# from typing import Annotated
# from fastapi import FastAPI, File, UploadFile , HTTPException
# import os
# import shutil
# import pymupdf
# import fitz



# app = FastAPI()


# UPLOAD_DIRECTORY = "uploads"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Create it if not exists

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     for i ,page in (file):
#        pdffile=fitz.open(file)
#        readfile=pdffile.load_page(i)
#        pdfextrat=readfile.extract()
#        pdfextrat.save(f"page.pdf")

#     return pdfextrat
#     return {"file_size": len(file)}
from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import shutil
import fitz  # pymupdf

app = FastAPI()

UPLOAD_DIRECTORY = "uploads"
EXTRACTED_TEXT_DIR = "extracted_texts"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Ensure directory exists

@app.post("/uploadfile/")
async def upload_and_extract(file: UploadFile = File(...)):
    try:
        # Save file to local directory
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Open PDF and extract text using PyMuPDF
        doc = fitz.open(file_path)
        extracted_text = ""
        for page in doc:
           extracted_text += page.get_text()
        doc.close()
        text_file_name = file.filename.replace(".pdf", ".txt")
        text_file_path = os.path.join(EXTRACTED_TEXT_DIR, text_file_name)
        with open(text_file_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        return {
            "message": "✅ Text extracted and saved successfully",
            "pdf_file": file.filename,
            "text_file": text_file_name,
            "saved_at": text_file_path}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9002, reload=True)
