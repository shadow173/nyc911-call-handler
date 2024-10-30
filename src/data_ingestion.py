# src/data_ingestion.py

import re

def preprocess_transcription(transcription):
    """
    Preprocess the transcription text.
    """
    # Remove special characters
    transcription = re.sub(r'[^A-Za-z0-9\s]', '', transcription)
    # Convert to lowercase
    transcription = transcription.lower()
    # Additional preprocessing steps...
    return transcription
