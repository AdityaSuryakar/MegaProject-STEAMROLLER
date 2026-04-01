# MegaProject
This Repository contains all the files ,codes ,datasets and synopsis of MegaProject

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
├── audio/                  → (input optional)
├── output/                 → generated files
│
└── requirements.txt
