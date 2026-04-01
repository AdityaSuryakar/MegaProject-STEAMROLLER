📌 MegaProject – STEAMROLLER
🎤 AI-Based Real-Time Speech Repair System

This repository contains all files, code, datasets, and implementation for STEAMROLLER, a real-time AI system designed to repair disfluent speech for People Who Stutter (PWS).

🚀 Project Overview

STEAMROLLER converts stuttering speech into clear, fluent, and meaningful speech using a multi-stage AI pipeline:

🎤 Speech Input → 🧠 ASR → 🔍 NLP Processing → 🤖 Multi-Agent Repair → 🔊 Text-to-Speech

It ensures:

✔ Removal of repetitions & prolongations
✔ Preservation of meaning
✔ Natural speech output
✨ Key Features
🎤 Live Mic Input – Capture real-time speech
📝 Speech-to-Text (ASR) – Powered by Whisper
🤖 Multi-Agent Repair System – Fix disfluencies intelligently
🧠 Master Agent Evaluation – Selects best output
🔊 Fluent Speech Output (TTS) – Natural audio generation
⚙️ Interactive Streamlit UI – Clean and user-friendly
📁 Project Structure
steamroller_full_project/
│
├── app/
│   └── app.py              → Streamlit UI
│
├── modules/
│   ├── asr.py              → Whisper ASR
│   ├── nlp.py              → Tokenization
│   ├── repair_agents.py    → AI repair logic
│   ├── coordinator.py      → Multi-agent pipeline
│   └── tts.py              → Text-to-Speech
│
├── utils/
│   └── realtime_input.py   → Mic recording
│
├── audio/                  → Optional input files
├── output/                 → Generated outputs
│
└── requirements.txt        → Dependencies
⚙️ Installation
git clone <your-repo-link>
cd steamroller_full_project
pip install -r requirements.txt
▶️ Run the Application
streamlit run app/app.py
🧠 Technologies Used
Frontend/UI: Streamlit
Backend: Python
ASR: OpenAI Whisper
NLP: Regex + Tokenization
AI Agents: Custom Multi-Agent System
TTS: Transformer-based Speech Synthesis
🎯 Use Cases
🧑‍🎓 Students & Presentations
💼 Interviews & Professional Communication
📞 Call Centers & Customer Support
♿ Assistive Technology for PWS
📊 Impact
🌍 Improves accessibility for 80M+ people who stutter
💬 Enhances confidence in communication
⚡ Enables real-time speech correction
🧩 Scalable to multiple languages & speech disorders
🔮 Future Enhancements
🎙️ Continuous real-time streaming
🎭 Voice cloning (personalized speech)
🌐 Multilingual support
📊 Live waveform visualization
👨‍💻 Author

Aditya Suryakar
AI/ML Developer | Speech Processing Enthusiast

⭐ Acknowledgment

This project is developed as part of a Mega Project / Hackathon solution focusing on Speech & Language Processing using AI Agents.
