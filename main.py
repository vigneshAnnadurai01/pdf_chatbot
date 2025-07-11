from typing import Annotated
from fastapi import FastAPI, File, UploadFile , HTTPException
import os
import shutil
import fitz 
import pdfplumber
from sentence_transformers import SentenceTransformer




app = FastAPI()


UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Create it if not exists


# ✅ Define your target directory (folder to save files)
# UPLOAD_DIRECTORY = "uploads"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Create it if not exists



@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    pdffile=fitz.open
    return {"file_size": len(file)}



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    try:
        # ✅ Get the file path where you want to save
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

        # ✅ Save uploaded file to local directory
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        extracted_text = ''
# extract text using pdfplnumber 
        with pdfplumber.open(file_path) as pdf:
         for page in pdf.pages:
           page_text = page.extract_text()
           if page_text:
               extracted_text+= page_text + "\n"

  # Step 3: Split into phrases and save each phrase in a new line
        phrases = [phrase.strip() for phrase in page_text.replace('\n', ' ').split('.') if phrase.strip()]

        # Step 4: Save phrases to .txt file
        txt_path = file_path.replace(".pdf", "_phrases.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            for phrase in phrases:
                f.write(phrase + ".\n")

 


            model = SentenceTransformer('all-MiniLM-L6-v2')
            with open(txt_path, "r", encoding="utf-8") as txt_file:
                    text = txt_file.read()
            vector = model.encode(text)


            # print(vector)  # This is the embedding (a 384-dimensional vector)






        return {
            "message": "✅ File uploaded and saved successfully.",
            "filename": file.filename,
            "total_phrases": len(phrases),
            "saved_to": txt_path,
            "chunk": vector.tolist()

        }



    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=f"❌ Failed to save file: {str(e)}")





   
if __name__ == "__main__":
    import uvicorn 
    
    uvicorn.run("main:app",host="0.0.0.0",port=9002)



