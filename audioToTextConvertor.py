import whisper
import os

# Load model once
model = whisper.load_model("tiny")

# List ALL audio files manually here (18 files)
audio_files = [
    "M_0030_16y4m_1.wav",
    "M_0061_16y9m-1.wav",
    "M_0078_16y5m_1.wav",
    "M_0107_07y7m_1.wav",
    "M_0121_11y1m_1.wav",
    "M_0121_15y1m_1.wav",
    "M_0553_10y0m_1.wav",
    "M_0553_11y0m_1.wav",
    "M_1022_11y3m_1.wav",
    "M_1023_11y3m_1.wav",
    "M_1064_47y0m_1.wav",
    "M_1099_25y0m_1.wav",
    "M_1100_28y0m_1.wav",
    "M_1101_35y0m_1.wav",
    "M_1103_20y0m_1.wav",
    "M_1104_40y0m_1.wav",
    "M_1105_21y0m_1.wav",
    "M_1106_25y0m_1.wav"

]

for audio in audio_files:
    print(f"Transcribing: {audio}")

    # Transcribe
    result = model.transcribe(audio)

    # Create txt file name (same name as audio)
    txt_file = os.path.splitext(audio)[0] + ".txt"

    # Write multiline transcript
    with open(txt_file, "w", encoding="utf-8") as file:
        for segment in result["segments"]:
            file.write(segment["text"].strip() + "\n")

    print(f"Saved: {txt_file}\n")

print("All 18 files transcribed successfully ✅")
