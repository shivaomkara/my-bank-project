from fastapi import FastAPI, UploadFile, File
from parser import extract_pdf_text
from pydantic import BaseModel
from ai_engine import ask_ai, extract_bank_data, fill_template, ask_document_question
import os
import json

app = FastAPI()
class QuestionRequest(BaseModel):
    document_text: str
    question: str

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

    try:
        draft_json = json.loads(draft)

        return {
            "filename": file.filename,
            "draft": draft_json
        }

    except Exception as e:

        return {
            "filename": file.filename,
            "draft": draft,
            "error": str(e)
        }
@app.post("/ask-question")
def ask_question(data: QuestionRequest):

    answer = ask_document_question(
        data.document_text,
        data.question
    )

    return {
        "question": data.question,
        "answer": answer
    }