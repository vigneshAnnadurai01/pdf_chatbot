# import pdfplumber

# with pdfplumber.open("example.pdf") as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()
#         print(text)
 


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



# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     pdffile=fitz.open
#     with pdfplumber.open("example.pdf") as pdf:
#      for page in pdf.pages:
#         text = page.extract_text()
#         print(text)
#     with open("output.txt", "w", encoding="utf-8") as f:
#      f.write(text)  # from above extraction


#     return {"file_size": len(file)}





@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    pdffile=fitz.open
    return {"file_size": len(file)}


