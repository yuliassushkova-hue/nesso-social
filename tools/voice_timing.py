"""When each sentence of a voice-over is spoken, so the captions follow the voice.

    python tools/voice_timing.py it-1 "First sentence." "Second sentence." ...

Whisper (faster-whisper, model "tiny") hears the recording in ~/Documents/GitHub/nesso-assets/voice/
<name>.mp3 and gives a time for every word it heard. Its spelling is not used: sentence k starts at the
word whose position matches the words in the script before it, scaled to the number of words heard.
The answer is written beside the recording as <name>.json: [[start, end, sentence], ...] and the length.
"""
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

VOICE = Path("~/Documents/GitHub/nesso-assets/voice").expanduser()


def hear(path):
    with tempfile.NamedTemporaryFile(suffix=".wav") as w:
        subprocess.run(["afconvert", "-f", "WAVE", "-d", "LEI16@16000", "-c", "1", str(path), w.name], check=True)
        with wave.open(w.name) as r:
            audio = np.frombuffer(r.readframes(r.getnframes()), np.int16).astype(np.float32) / 32768
    segments, info = WhisperModel("tiny", device="cpu", compute_type="int8").transcribe(audio, word_timestamps=True)
    words = [w for s in segments for w in s.words]
    return words, info.duration


def main(name, sentences):
    words, length = hear(VOICE / f"{name}.mp3")
    counts = [len(s.split()) for s in sentences]
    total, scale = sum(counts), len(words) / sum(counts)
    starts, before = [], 0
    for c in counts:
        starts.append(words[min(len(words) - 1, round(before * scale))].start)
        before += c
    ends = starts[1:] + [words[-1].end]
    out = {"length": round(length, 2), "lines": [[round(a, 2), round(b, 2), s] for a, b, s in zip(starts, ends, sentences)]}
    (VOICE / f"{name}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for a, b, s in out["lines"]:
        print(f"{a:5.1f}–{b:5.1f}  {s}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
