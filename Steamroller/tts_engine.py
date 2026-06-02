"""
tts_engine.py — Fast speech synthesis.

Note: This project does not perform true voice cloning. True cloning needs a
voice-conversion/TTS model such as XTTS/YourTTS and a reference speaker sample.
For speed, this module uses local system TTS and tries to choose a male/system
voice to avoid the default female gTTS voice.
"""

import io
import os
import tempfile
from typing import Literal

TTSBackend = Literal["pyttsx3", "gtts"]


def text_to_speech_pyttsx3(text: str, prefer_male: bool = True, rate: int = 165) -> bytes:
    import pyttsx3

    engine = pyttsx3.init()
    engine.setProperty("rate", rate)

    voices = engine.getProperty("voices") or []
    chosen_voice_id = None
    if prefer_male:
        male_keywords = ["male", "david", "mark", "ravi", "zira"]
        for voice in voices:
            desc = f"{getattr(voice, 'id', '')} {getattr(voice, 'name', '')}".lower()
            if any(k in desc for k in male_keywords) and "zira" not in desc:
                chosen_voice_id = voice.id
                break
    if not chosen_voice_id and voices:
        chosen_voice_id = voices[0].id
    if chosen_voice_id:
        engine.setProperty("voice", chosen_voice_id)

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.close()
    try:
        engine.save_to_file(text, tmp.name)
        engine.runAndWait()
        with open(tmp.name, "rb") as f:
            return f.read()
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass


def text_to_speech_gtts(text: str, lang: str = "en", slow: bool = False) -> bytes:
    from gtts import gTTS
    tts = gTTS(text=text, lang=lang, slow=slow)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    return buf.getvalue()


def synthesise_speech(text: str, backend: TTSBackend = "pyttsx3", lang: str = "en", slow: bool = False) -> bytes:
    if not text.strip():
        raise ValueError("Cannot synthesise empty text.")
    if backend == "gtts":
        try:
            return text_to_speech_gtts(text, lang=lang, slow=slow)
        except Exception:
            return text_to_speech_pyttsx3(text)
    return text_to_speech_pyttsx3(text)
