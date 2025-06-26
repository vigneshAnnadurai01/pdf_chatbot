from typing import Annotated
from fastapi import FastAPI, File, UploadFile , HTTPException
import os
import shutil
import pymupdf
import fitz 
import pdfplumber



app = FastAPI()


UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Create it if not exists

app = FastAPI()

# ✅ Define your target directory (folder to save files)
# UPLOAD_DIRECTORY = "uploads"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Create it if not exists



@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    pdffile=fitz.ope
    return {"file_size": len(file)}



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    try:
        # ✅ Get the file path where you want to save
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

        # ✅ Save uploaded file to local directory
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)


        return {
            "message": "✅ File uploaded and saved successfully.",
            "filename": file.filename,
            "saved_to": file_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Failed to save file: {str(e)}")


            #   return {"filename": file.filename}
   
if __name__ == "__main__":
    import uvicorn 
    
    uvicorn.run("main:app",host="0.0.0.0",port=9002)



