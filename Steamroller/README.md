<div align="center">

# 🎙️ STEAMROLLER
### Multi-Agent Speech Repair & Fluency Enhancement Assistant

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Whisper](https://img.shields.io/badge/ASR-OpenAI%20Whisper-000000?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/whisper)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![F5-TTS](https://img.shields.io/badge/Voice%20Cloning-F5--TTS-792EE5?style=for-the-badge)](https://github.com/SWivid/F5-TTS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Transforming speech affected by repetitions, prolongations, blocks, and fillers into clean, fluent, and natural audio.</b>
</p>

[Overview](#-overview) •
[Key Features](#-key-features) •
[Architecture](#-system-architecture) •
[Multi-Agent Design](#-multi-agent-system) •
[Master Agent & Scoring](#-master-agent--evaluation-loop) •
[Quickstart](#-installation--quickstart) •
[Voice Cloning](#-optional-f5-tts-voice-cloning) •
[Project Structure](#-project-structure) •
[Roadmap](#-limitations--future-roadmap)

---

</div>

## 📖 Overview

**STEAMROLLER** is an intelligent, multi-agent speech repair pipeline engineered to assist individuals who stutter or experience speech disfluencies. By combining robust automatic speech recognition (ASR), rule-based NLP cleaning, four specialized parallel repair agents, and a heuristic Master Agent evaluation loop, STEAMROLLER accurately repairs speech while preserving speaker intent and voice identity.

> [!NOTE]
> STEAMROLLER is designed for near real-time desktop usage with fast sub-minute processing on consumer hardware using local models, with optional zero-shot voice cloning powered by F5-TTS.

---

## ✨ Key Features

| Capability | Description |
| :--- | :--- |
| 🔁 **Repetition Removal** | Detects and resolves syllable-level (`b-b-because`), word-level (`I I I want`), and phrase-level restarts. |
| 〰️ **Prolongation Cleanup** | Normalizes sound elongations, stuttered character repeats, and phonetic blocks (`soooo` → `so`). |
| 🗣️ **Filler Word Filtering** | Filters conversational disfluencies and fillers (`uh`, `um`, `er`, `you know`, `like`, `actually`). |
| ⚡ **Parallel Multi-Agent Repair** | Concurrently generates 4 specialized repair candidates via Python's `ThreadPoolExecutor`. |
| 🧠 **Heuristic Master Agent** | Evaluates candidate quality across 4 weighted dimensions with automated feedback loops (up to 3 iterations). |
| 🧬 **Zero-Shot Voice Cloning** | Optional integration with remote **F5-TTS** backend to synthesize repaired text in the speaker's original voice. |
| 🖥️ **Interactive Streamlit UI** | Real-time audio waveform visualizer, side-by-side transcript diffs, execution logs, and audio playback. |

---

## 🏗️ System Architecture

### Pipeline Flowchart

```mermaid
flowchart TD
    A["🎙️ Input Audio<br/>(Recorded / Uploaded WAV/MP3)"] --> B["📝 Whisper ASR<br/>(Local 'tiny' model)"]
    B --> C["🧹 NLP Preprocessing & Cleaning<br/>(Syllable & word repetition removal)"]
    
    subgraph ParallelAgents ["⚡ Parallel Repair Agents (ThreadPoolExecutor)"]
        direction TB
        D1["🛡️ Meaning Preservation Agent"]
        D2["✍️ Grammar Optimized Agent"]
        D3["✂️ Concise Fluent Agent"]
        D4["🔗 Sequence Optimized Agent"]
    end
    
    C --> D1
    C --> D2
    C --> D3
    C --> D4
    
    D1 --> E["📦 Candidate Outputs Pool"]
    D2 --> E
    D3 --> E
    D4 --> E
    
    E --> F{"🧠 Master Agent Evaluation<br/>(Weighted Scoring Matrix)"}
    
    F -->|"Combined Score ≥ 0.80"| G["🏆 Best Candidate Selected"]
    F -->|"Score < 0.80 & Iteration < 3"| H["🔄 Iterative Feedback Loop<br/>(Feed highest candidate back)"]
    H -->|Refined Token Sequence| ParallelAgents
    
    G --> I{"🔊 Text-to-Speech Engine"}
    I -->|"Default"| J1["💻 Local System TTS (pyttsx3 / gTTS)"]
    I -->|"Voice Clone Mode"| J2["🧬 Remote F5-TTS Server (Kaggle/GPU)"]
    
    J1 --> K["🎧 Repaired, Fluent Audio Output"]
    J2 --> K

    style A fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style G fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style K fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style F fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style ParallelAgents fill:#fafafa,stroke:#9e9e9e,stroke-width:1px
```

### ASCII Architecture

```text
Input Audio
    │
    ▼
Whisper ASR
    │
    ▼
NLP Cleaning (Filler removal, Syllable & phrase deduplication)
    │
    ▼
┌────────────────────────────────────────────────────────┐
│             Parallel Repair Agents                     │
│  ├── 1. Meaning Preservation Agent                     │
│  ├── 2. Grammar Optimized Agent                        │
│  ├── 3. Concise Fluent Agent                           │
│  └── 4. Sequence Optimized Agent                       │
└────────────────────────────────────────────────────────┘
    │
    ▼
Candidate Outputs
    │
    ▼
Master Agent Evaluation
    ├── Meaning Preservation Score (50%)
    ├── Grammar Quality Score      (30%)
    ├── Concise Fluency Score      (15%)
    └── Sequence Similarity Score  (5%)
    │
    ▼
Threshold Check (Score ≥ 0.80)
    ├── [Passed]      ──► Final Selected Output
    └── [Not Met]     ──► Feedback Iteration (Max 3 cycles)
                                │
                                └──► Feed back into Parallel Agents
    │
    ▼
Text-to-Speech Engine (Local pyttsx3/gTTS or Remote F5-TTS)
    │
    ▼
Repaired, Fluent Audio
```

---

## 🤖 Multi-Agent System

Rather than relying on a single monolithic prompt, STEAMROLLER coordinates four dedicated, lightweight repair agents executing concurrently via `concurrent.futures.ThreadPoolExecutor`:

```
                                  ┌───────────────────────────────┐
                                  │   Pre-Cleaned ASR Transcript  │
                                  └──────────────┬────────────────┘
                                                 │
                   ┌─────────────────────────────┼─────────────────────────────┐
                   ▼                             ▼                             ▼
       ┌───────────────────────┐     ┌───────────────────────┐     ┌───────────────────────┐
       │  Meaning Preservation │     │   Grammar Optimized   │     │    Concise Fluent     │
       │         Agent         │     │         Agent         │     │         Agent         │
       └───────────┬───────────┘     └───────────┬───────────┘     └───────────┬───────────┘
                   │                             │                             │
                   └─────────────────────────────┼─────────────────────────────┘
                                                 ▼
                                     ┌───────────────────────┐
                                     │   Sequence Optimized  │
                                     │         Agent         │
                                     └───────────────────────┘
```

### 1. 🛡️ Meaning Preservation Agent
- **Focus**: Maximum semantic fidelity.
- **Mechanism**: Prunes low-level conversational hesitation markers (`uh`, `um`, `ah`, `er`, `you know`) while leaving sentence clauses and vocabulary intact.
- **Normalization**: Preserves sentence boundaries, normalizes casing and trailing terminal punctuation.

### 2. ✍️ Grammar Optimized Agent
- **Focus**: Structural correctness & orthography.
- **Mechanism**: Resolves split contractions (`can not` → `cannot`), missing apostrophes (`dont` → `don't`, `cant` → `can't`), and cleans awkward spacing around punctuation marks.

### 3. ✂️ Concise Fluent Agent
- **Focus**: Redundancy elimination and flow.
- **Mechanism**: Strips conversational hedges (`basically`, `actually`, `like`), deduplicates consecutive duplicate words (`I I want` → `I want`), and collapses elongated letter repetitions (`soooo` → `so`).

### 4. 🔗 Sequence Optimized Agent
- **Focus**: Stutter fragment repair & sequence smoothing.
- **Mechanism**: Resolves hyphenated syllable restart fragments from ASR (`I-I-I` or `w-w-want`), collapses repeated multi-word token sequences, and ensures proper capitalization.

---

## 🎯 Master Agent & Evaluation Loop

The **Master Agent** manages candidate evaluation, quality thresholding, and the iterative feedback loop.

### 📊 Scoring Weights & Metrics

Every candidate generated by the parallel agents is evaluated across four objective heuristic metrics:

| Metric | Weight | Measurement Strategy | Description |
| :--- | :---: | :--- | :--- |
| **Meaning Preservation** | `50%` | Character `SequenceMatcher.ratio()` | Ensures the repaired output remains semantically faithful to the original transcript. |
| **Grammar Quality** | `30%` | Capitalization, terminal punctuation, whitespace rules | Verifies sentence capitalization, terminal punctuation (`.`, `!`, `?`), and absence of double spaces or detached commas. |
| **Concise Fluency** | `15%` | Consecutive word repetition ratio ($1 - \frac{N_{repeats}}{N_{words}}$) | Penalizes stutters, redundant word loops, and unnatural repetitions. |
| **Sequence Similarity** | `5%` | Token-level `SequenceMatcher.ratio()` | Ensures natural syntactic word order is preserved between input and candidate. |

$$\text{Final Score} = 0.50 \cdot S_{\text{meaning}} + 0.30 \cdot S_{\text{grammar}} + 0.15 \cdot S_{\text{fluency}} + 0.05 \cdot S_{\text{sequence}}$$

### 🔄 The Feedback Decision Logic

1. **Threshold Assessment**: Each candidate's composite score is checked against the threshold of **`0.80`**.
2. **Success Exit**: If one or more candidates meet or exceed `0.80`, the candidate with the highest composite score is immediately selected as the final verdict.
3. **Feedback Refinement**: If no candidate reaches `0.80`, the current highest-scoring candidate text is re-tokenized and fed back into the parallel agents as the input for the next cycle.
4. **Iteration Cap**: Bounded to a maximum of **3 iterations**. If the threshold is still not met after 3 cycles, the highest-scoring candidate across all iterations is returned with status `threshold_not_met`.
5. **Execution State**: All intermediate candidate outputs, individual metric scores, and iteration trails are preserved for auditing and UI inspection.

---

## 🛠️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Core & UI** | Python 3.10+, Streamlit |
| **Speech Recognition** | OpenAI Whisper (`tiny` default for high-speed local inference) |
| **NLP & Text Processing** | NLTK, Python `re`, `difflib.SequenceMatcher` |
| **Deep Learning & Audio** | PyTorch, NumPy, SciPy |
| **Local TTS Engines** | `pyttsx3` (Offline native OS voices), `gTTS` (Google Translate TTS) |
| **Voice Cloning** | **F5-TTS** (Non-autoregressive flow matching zero-shot TTS) |
| **Remote Backend** | Flask, pyngrok (for GPU server tunneling) |

---

## 📁 Project Structure

```text
STEAMROLLER/
├── app.py                     # Streamlit frontend & interactive dashboard
├── audio_pipeline.py          # Audio pre-processing & Whisper ASR pipeline
├── nlp_cleaner.py             # Rule-based regex cleaner & repetition detector
├── repair_agents.py           # Specialized repair agents & single-agent repairs
├── repair_agents_runner.py    # ThreadPoolExecutor runner for parallel agent execution
├── master_agent.py            # Master Agent scoring, thresholding & feedback loop
├── tts_engine.py              # Local TTS dispatcher (pyttsx3 & gTTS)
├── voice_clone.py             # Thin HTTP client for remote F5-TTS server
├── kaggle_server_cell.py      # Production Flask + ngrok server cell for Kaggle/Colab GPU
├── requirements.txt           # Python dependencies
└── README.md                  # System documentation
```

### Main Components Overview

- [app.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/app.py): Streamlit dashboard with file uploader, microphone recorder, audio player, agent outputs, and iteration state debugger.
- [audio_pipeline.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/audio_pipeline.py): Loads Whisper model, normalizes incoming audio samples to 16kHz mono, and extracts raw text.
- [nlp_cleaner.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/nlp_cleaner.py): Detects syllable stutters (`b-b-`), word/phrase repetitions, and cleans common fillers.
- [repair_agents.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/repair_agents.py): Defines `MeaningPreservationAgent`, `GrammarOptimizedAgent`, `ConciseFluentAgent`, and `SequenceOptimizedAgent`.
- [repair_agents_runner.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/repair_agents_runner.py): Concurrently runs all agents across CPU worker threads.
- [master_agent.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/master_agent.py): Computes heuristic metrics, manages candidate selection, and drives iterative feedback.
- [tts_engine.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/tts_engine.py): Synthesizes fluent speech using local engines.
- [voice_clone.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/voice_clone.py): Streams synthesized voice cloning requests to remote F5-TTS servers.
- [kaggle_server_cell.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/kaggle_server_cell.py): Ready-to-run Jupyter/Kaggle cell for zero-shot F5-TTS inference.

---

## 🚀 Installation & Quickstart

### Prerequisites
- Python `3.10` or higher
- `ffmpeg` installed on your system (required for Whisper audio decoding)

### 1. Clone & Install Dependencies

```bash
# Clone the repository
git clone https://github.com/your-username/steamroller.git
cd steamroller

# Create a virtual environment (recommended)
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch Streamlit Application

```bash
streamlit run app.py
```

> [!TIP]
> **Performance Recommendation**: The default Whisper model is configured to `tiny` for rapid inference. For best latency (under 60 seconds), use audio recordings between **5 and 30 seconds**.

---

## 🧬 Optional F5-TTS Voice Cloning

By default, STEAMROLLER uses local offline TTS (`pyttsx3` or `gTTS`). If you want the repaired audio to sound identical to the user's natural voice, you can connect STEAMROLLER to an external **F5-TTS** GPU backend.

```
┌───────────────────────────┐                     ┌───────────────────────────────┐
│     Local STEAMROLLER     │                     │     Remote GPU Host (Kaggle)  │
│  (Streamlit on localhost) │                     │  (F5-TTS Model + ngrok tunnel)│
└─────────────┬─────────────┘                     └───────────────┬───────────────┘
              │                                                   │
              │  POST /clone-voice                                │
              │  { "ref_audio": "...", "gen_text": "..." }        │
              ├──────────────────────────────────────────────────►│
              │                                                   │
              │  WAV Audio Stream                                 │
              │◄──────────────────────────────────────────────────┤
```

### Step-by-Step Setup

1. **Start Kaggle/Colab GPU Notebook**:
   - Open a Kaggle notebook and enable a GPU accelerator (T4 or P100).
   - Copy the code from [kaggle_server_cell.py](file:///d:/Projects/Steamroller_f5tts%20(2)/Steamroller/kaggle_server_cell.py) into a notebook cell after installing F5-TTS.
   - Run the cell — it will spin up a Flask server and display a public ngrok tunnel URL (e.g. `https://abcd-1234.ngrok-free.app`).

2. **Set the Environment Variable**:
   
   **Windows PowerShell:**
   ```powershell
   $env:KAGGLE_TTS_URL="https://YOUR-NGROK-URL.ngrok-free.app"
   streamlit run app.py
   ```

   **Linux / macOS (Bash):**
   ```bash
   export KAGGLE_TTS_URL="https://YOUR-NGROK-URL.ngrok-free.app"
   streamlit run app.py
   ```

3. **Select Voice in App**:
   - In the Streamlit sidebar, select **"F5-TTS Voice Clone"** as the TTS output engine.
   - STEAMROLLER will transmit the original audio as reference and synthesize the repaired text in the speaker's cloned voice!

---

## 📈 Evaluation & State Tracking

STEAMROLLER maintains full execution state throughout each session for diagnostic and research transparency:

- 📝 **Original Raw Transcript**: Initial transcription produced by Whisper ASR.
- 🧹 **Cleaned Transcript**: Pre-processed text after regex and syllable deduplication.
- 📦 **Per-Iteration Candidate Pool**: Outputs generated by each of the 4 agents.
- 📊 **Fine-Grained Score Breakdown**: Meaning (50%), Grammar (30%), Fluency (15%), Sequence (5%).
- 🏆 **Final Selection & Iteration Count**: Detailed reasoning and final convergence status (`success` vs `threshold_not_met`).

---

## ⚠️ Limitations & Future Roadmap

### Current Limitations
- **Heuristic Evaluation**: Current scoring metrics use heuristic string algorithms (`SequenceMatcher`, regex) rather than learned neural reward models.
- **Rule-Based Repair Agents**: Repair agents rely on deterministic pattern matching rather than generative Large Language Models.
- **Asynchronous Processing**: Optimized for pre-recorded or short uploaded clips rather than full-duplex real-time streaming speech.
- **Voice Cloning Infrastructure**: High-quality zero-shot voice cloning requires an external GPU instance.

### Future Roadmap
- [ ] **LLM-Powered Repair Agents**: Introduce a small quantized local LLM (e.g., Llama 3 8B or Mistral 7B) for context-aware pragmatic repair.
- [ ] **Learned Speech-Repair Metrics**: Train a neural sentence fluency scorer calibrated on human perception ratings.
- [ ] **Real-Time Streaming Pipeline**: Stream audio chunks with sub-second latency using WebRTC and streaming ASR.
- [ ] **Expanded Disfluency Benchmarking**: Evaluate against open-source stutter datasets (e.g., SEP-28k, FluencyBank) for rigorous quantitative validation.

---

<div align="center">

Built with ❤️ for accessible, fluent, and empowering speech communication.

</div>
