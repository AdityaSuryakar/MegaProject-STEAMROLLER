"""
audio_pipeline.py — Upload audio + optimized Whisper ASR transcription.
"""

import io
import os
import wave
import tempfile
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write as wav_write

SAMPLE_RATE = 16000
CHANNELS = 1


def record_audio(duration_seconds: int = 10) -> np.ndarray:
    audio = sd.rec(int(duration_seconds * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype="float32")
    sd.wait()
    return audio.flatten()


def numpy_to_wav_bytes(audio: np.ndarray, sample_rate: int = SAMPLE_RATE) -> bytes:
    audio_int16 = (audio * 32767).astype(np.int16)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_int16.tobytes())
    return buf.getvalue()


def save_audio_to_temp(audio: np.ndarray) -> str:
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav_write(tmp.name, SAMPLE_RATE, (audio * 32767).astype(np.int16))
    return tmp.name


_whisper_models = {}


def _load_whisper(model_size: str = "tiny"):
    if model_size not in _whisper_models:
        import whisper
        _whisper_models[model_size] = whisper.load_model(model_size)
    return _whisper_models[model_size]


def transcribe_audio(audio: np.ndarray, model_size: str = "tiny", language: Optional[str] = None) -> Tuple[str, dict]:
    model = _load_whisper(model_size)
    tmp_path = save_audio_to_temp(audio)
    try:
        result = model.transcribe(tmp_path, language=language, verbose=False, fp16=False, beam_size=1, best_of=1, condition_on_previous_text=False)
    finally:
        os.unlink(tmp_path)
    return result["text"].strip(), result


def transcribe_uploaded_file(file_bytes: bytes, filename: str = "audio.wav", model_size: str = "tiny", language: Optional[str] = None) -> Tuple[str, dict]:
    model = _load_whisper(model_size)
    suffix = Path(filename).suffix or ".wav"
    tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    tmp.write(file_bytes)
    tmp.flush()
    tmp.close()
    try:
        result = model.transcribe(tmp.name, language=language, verbose=False, fp16=False, beam_size=1, best_of=1, condition_on_previous_text=False)
    finally:
        os.unlink(tmp.name)
    return result["text"].strip(), result
