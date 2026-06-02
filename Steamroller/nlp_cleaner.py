from dataclasses import dataclass
from repair_agents import clean_stutter


@dataclass
class CleanReport:
    original: str
    cleaned: str


def clean_asr_output(text):
    if not text:
        return CleanReport(original="", cleaned="")

    cleaned = clean_stutter(text)

    return CleanReport(
        original=text,
        cleaned=cleaned
    )