from fastapi import FastAPI, UploadFile, File
from parser import extract_pdf_text
from ai_engine import ask_ai, extract_bank_data, fill_template
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {
        "message": "Bank Document AI Running"
    }

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_pdf_text(file_path)

    return {
        "filename": file.filename,
        "text": extracted_text
    }
@app.post("/extract-bank-data")
async def extract_data(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_pdf_text(file_path)

    ai_result = extract_bank_data(extracted_text)

    return {
        "filename": file.filename,
        "ai_result": ai_result
    }
@app.post("/generate-draft")
async def generate_draft(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_pdf_text(file_path)

    draft = fill_template(extracted_text)

    return {
        "filename": file.filename,
        "draft": draft
    }