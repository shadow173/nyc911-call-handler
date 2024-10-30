
from pydub import AudioSegment
import numpy as np
import librosa
import soundfile as sf
import noisereduce as nr
import os



def convert_to_wav(input_file_path):
    if input_file_path.lower().endswith('.wav'):
        return input_file_path  # No conversion needed
    else:
        audio = AudioSegment.from_file(input_file_path)
        wav_file_path = os.path.splitext(input_file_path)[0] + ".wav"
        audio.export(wav_file_path, format="wav")
        return wav_file_path
def noise_reduction(y, sr):
    # Estimate noise from a section of the audio (e.g., first 0.5 seconds)
    noise_sample = y[:int(sr * 0.5)]
    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=y, y_noise=noise_sample, sr=sr)
    return reduced_noise
def process_audio(input_file_path, output_directory):
    # Convert input file to WAV if necessary
    wav_file_path = convert_to_wav(input_file_path)

    # Load audio file
    y, sr = librosa.load(wav_file_path, sr=None)

    # Perform noise reduction
    y_reduced = noise_reduction(y, sr)

    # Save the cleaned audio
    filename = os.path.basename(wav_file_path)
    processed_file_path = os.path.join(output_directory, f"cleaned_{filename}")
    sf.write(processed_file_path, y_reduced, sr)

    return processed_file_path