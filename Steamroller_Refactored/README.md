<div align="center">

# 🎙️ STEAMROLLER (Refactored)
### Multi-Agent Speech Repair & Zero-Shot F5-TTS Voice Cloning Architecture

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Whisper](https://img.shields.io/badge/ASR-OpenAI%20Whisper-000000?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/whisper)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![F5-TTS](https://img.shields.io/badge/Voice%20Cloning-F5--TTS-792EE5?style=for-the-badge)](https://github.com/SWivid/F5-TTS)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

<p align="center">
  <b>Decoupled, modular multi-agent pipeline transforming stuttered or disfluent speech into fluent, natural speech synthesized in the speaker's own cloned voice.</b>
</p>

---

</div>

## 📌 Architecture Highlights

This refactored architecture provides complete separation of concerns between UI, orchestration, ASR, NLP cleaning, multi-agent repair, and remote GPU voice cloning services:

```mermaid
flowchart TD
    subgraph Client ["💻 Client / Local Laptop"]
        UI["Streamlit UI (ui/, app.py)"] --> Pipeline["Pipeline Runner (pipeline.py)"]
        Pipeline --> ASR["Whisper ASR (asr/whisper_asr.py)"]
        ASR --> NLP["NLP Cleaner (nlp/cleaner.py)"]
        NLP --> Agents["Multi-Agent Repair & Scoring (agents/repair_agents.py)"]
        Agents --> F5Client["F5-TTS Client (tts/f5_tts_client.py)"]
        Settings["Centralized Config (config/settings.py)"] -.-> Pipeline
        Settings -.-> F5Client
        KaggleService["Kaggle Auto-Launch / Health (services/kaggle_gpu.py)"] -.-> F5Client
    end

    subgraph Remote ["⚡ Remote Kaggle GPU Backend"]
        FastAPIServer["FastAPI Server (kaggle_server/f5_tts_server.py)"]
        Tunnel["pyngrok Public Tunnel"]
        F5Model["F5-TTS Zero-Shot DiT Model (Warm in GPU VRAM)"]

        Tunnel --> FastAPIServer
        FastAPIServer --> F5Model
    end

    F5Client == "POST /clone (Multipart Audio + Cleaned Text)" ==> Tunnel
    FastAPIServer == "Cloned Repaired Audio Stream (WAV)" ==> F5Client
```

---

## 📁 Directory Structure

```text
Steamroller_Refactored/
├── app.py                      # Streamlit interactive frontend
├── pipeline.py                 # Core headless pipeline orchestrator
├── requirements.txt            # Local Python dependencies
├── .env.example                # Example configuration and environment template
├── .gitignore                  # Git ignore rules for caches, .env, and runtime audio
├── config/
│   ├── __init__.py
│   └── settings.py             # Centralized settings & environment loader
├── asr/
│   ├── __init__.py
│   └── whisper_asr.py          # OpenAI Whisper speech-to-text inference
├── nlp/
│   ├── __init__.py
│   └── cleaner.py              # Stutter pattern, syllable repeat & filler removal
├── agents/
│   ├── __init__.py
│   └── repair_agents.py        # 4 specialized repair agents + heuristic evaluator
├── services/
│   ├── __init__.py
│   └── kaggle_gpu.py           # Kaggle API kernel auto-launch & health service
├── tts/
│   ├── __init__.py
│   └── f5_tts_client.py        # Zero-shot F5-TTS remote client
├── ui/
│   ├── __init__.py
│   ├── recorder.py             # Audio input recorder & upload handling
│   └── styles.py               # Modern responsive CSS styles
├── utils/
│   ├── __init__.py
│   ├── audio_utils.py          # Audio format conversion & normalization
│   └── errors.py               # Typed exception hierarchy
├── kaggle_server/
│   ├── f5_tts_server.py        # Production FastAPI server script for Kaggle cell
│   └── final-f5tts.ipynb       # Jupyter notebook for Kaggle GPU environment
├── outputs/                    # Runtime synthesized audio output directory
└── uploads/                    # Runtime user recording upload directory
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites
- Python 3.10+
- `ffmpeg` installed on your PATH

### 2. Install Dependencies
```bash
cd Steamroller_Refactored
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Environment Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Set your Kaggle ngrok endpoint in `.env`:
```ini
KAGGLE_TTS_URL="https://YOUR-NGROK-SUBDOMAIN.ngrok-free.dev"
```

Optional Kaggle API credentials for auto-launch:
```ini
KAGGLE_USERNAME="your-username"
KAGGLE_KEY="your-api-key"
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

---

## ☁️ Setting Up the Kaggle F5-TTS GPU Backend

1. Open Kaggle and create a new notebook with **GPU Accelerator (T4 x2 or P100)** enabled.
2. Open `kaggle_server/final-f5tts.ipynb` or paste the contents of `kaggle_server/f5_tts_server.py` as the execution cell.
3. Add your `NGROK_AUTH_TOKEN` under **Add-ons → Secrets**.
4. Run the notebook cell to launch the FastAPI server.
5. Copy the printed ngrok public URL into your `.env` as `KAGGLE_TTS_URL`.
