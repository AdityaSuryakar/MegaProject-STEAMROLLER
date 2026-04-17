import whisper
import os


# Load model once
model = whisper.load_model("tiny")

# Base directory (same folder as this script)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create output folder
output_folder = os.path.join(base_dir, "transcripts")
os.makedirs(output_folder, exist_ok=True)

# Audio folder path
audio_folder = os.path.join(base_dir, "audio")

# Get all .wav audio files automatically
audio_files = [
    os.path.join(audio_folder, f)
    for f in os.listdir(audio_folder)
    if f.endswith(".wav")
]

for audio in audio_files:
    print(f"Transcribing: {audio}")

    # Transcribe
    result = model.transcribe(audio)

    # Create txt file path inside folder
    txt_file = os.path.join(
        output_folder,
        os.path.splitext(os.path.basename(audio))[0] + ".txt"
    )

    # Write transcript
    with open(txt_file, "w", encoding="utf-8") as file:
        for segment in result["segments"]:
            file.write(segment["text"].strip() + "\n")

    print(f"Saved: {txt_file}\n")

print("All audio files transcribed successfully")
