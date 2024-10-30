# src/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
from .audio_processing import process_audio

app = FastAPI()

UPLOAD_DIRECTORY = "uploaded_files"
PROCESSED_DIRECTORY = "processed_files"

# Ensure directories exist
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
os.makedirs(PROCESSED_DIRECTORY, exist_ok=True)

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    # Check file extension
    if not file.filename.lower().endswith(('.wav', '.m4a')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only WAV and M4A files are accepted.")

    # Save the uploaded file
    upload_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the audio file
    try:
        processed_file_path = process_audio(upload_path, PROCESSED_DIRECTORY)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {e}")

    return {"message": "Audio file uploaded and processed successfully.", "processed_file": processed_file_path}
