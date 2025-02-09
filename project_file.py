import os
import whisper
import json
import ffmpeg
from pathlib import Path

def find_media_files(directory, extensions=(".mp3", ".wav", ".mp4", ".mkv", ".aac", ".flac")):
    """Recursively scan a directory for media files."""
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                media_files.append(os.path.join(root, file))
    return media_files

def transcribe_audio(file_path, model):
    """Transcribe an audio/video file using Whisper."""
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]
# ------------
def save_transcription(file_path, transcription, output_format="txt", output_dir="trans"):
    """Save transcription to a file (TXT or JSON)."""
    os.makedirs(output_dir, exist_ok=True)
    base_name = Path(file_path).stem
    output_file = os.path.join(output_dir, f"{base_name}.{output_format}")
    
    if output_format == "txt":
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcription)
    elif output_format == "json":
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"filename": file_path, "transcription": transcription}, f, indent=4)
    
    print(f"Saved: {output_file}")

def main(directory="media_folder", output_format="txt"):
    """Main function to scan, transcribe, and save results."""
    model = whisper.load_model("tiny") 
    media_files = find_media_files(directory)
    
    if not media_files:
        print("No media files found in the specified directory.")
        return
    
    for file in media_files:
        transcription = transcribe_audio(file, model)
        save_transcription(file, transcription, output_format)
    
    print("✅ Transcription completed for all files.")

if __name__ == "__main__":
    main("data_file", "txt")
