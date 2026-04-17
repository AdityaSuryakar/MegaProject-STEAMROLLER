# Audio to NLP Sentence Tokenizer Pipeline

A two-stage Python pipeline that:
1. **Transcribes** `.wav` audio files to text using OpenAI Whisper
2. **Tokenizes** the transcripts into sentences using NLTK

---

## Folder Structure

```
MegaProject-main/
│
├── audio/                        # Place your .wav audio files here (input)
│
├── transcripts/                  # Auto-created: Whisper transcription output (.txt)
│
├── tokens/                       # Auto-created: Sentence-tokenized output (.txt)
│
├── audioToTextConvertor.py       # Stage 1 - Transcribes audio to text
├── nlp_tokenizer.py              # Stage 2 - Tokenizes transcripts into sentences
└── README.md
```

---

## Prerequisites

### 1. Python
Make sure Python 3.8+ is installed.  
Download from: https://www.python.org/downloads/

### 2. FFmpeg
Required by Whisper to read audio files.

- Download from: https://ffmpeg.org/download.html  
- After installing, ensure `ffmpeg` is added to your **system PATH**  
- Verify with:
  ```powershell
  ffmpeg -version
  ```

### 3. Python Dependencies

Install required packages:

```powershell
pip install openai-whisper nltk
```

---

## How to Run

### Step 1 — Add your audio files

Place all `.wav` audio files inside the `audio/` folder:

```
MegaProject-main/
└── audio/
    ├── sample1.wav
    ├── sample2.wav
    └── ...
```

---

### Step 2 — Transcribe audio to text

Run the transcription script:

```powershell
cd "MegaProject-main"
python audioToTextConvertor.py
```

**What it does:**
- Loads all `.wav` files from the `audio/` folder
- Transcribes each using OpenAI Whisper (`tiny` model)
- Saves transcripts as `.txt` files in the `transcripts/` folder

> ⚠️ This runs on CPU by default and may take several minutes for large audio files.

**Example output:**
```
Transcribing: audio\sample1.wav
Saved: transcripts\sample1.txt

All audio files transcribed successfully
```

---

### Step 3 — Tokenize transcripts into sentences

Run the NLP tokenizer:

```powershell
python nlp_tokenizer.py
```

**What it does:**
- Reads all `.txt` files from the `transcripts/` folder
- Splits each transcript into individual sentences using NLTK
- Saves one sentence per line in the `tokens/` folder

**Example output:**
```
Processed sentence tokens saved: tokens\sample1_tokens.txt
NLP processing completed successfully.
```

---

## Output Format

### `transcripts/sample1.txt`
```
Hello my name is John and I am from New York.
I have been working in software for five years.
```

### `tokens/sample1_tokens.txt`
```
Hello my name is John and I am from New York.
I have been working in software for five years.
```
Each line = one sentence token.

---

## Notes

- The `transcripts/` and `tokens/` folders are **created automatically** — no need to create them manually.
- Scripts use **relative paths**, so they work from any location on your system.
- NLTK's `punkt` tokenizer data is downloaded automatically on first run.
- To use a more accurate Whisper model (slower), change `"tiny"` to `"base"`, `"small"`, or `"medium"` in `audioToTextConvertor.py`:
  ```python
  model = whisper.load_model("base")
  ```
  
