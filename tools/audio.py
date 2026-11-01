"""Sound for a Reel: a music bed and timed sound effects, mixed and put under the video.

Sounds and music are Mixkit's (free licence for social posts and ads), converted to WAV in
~/Documents/GitHub/nesso-assets/mixkit; see the LICENSE.md there. The mix is written as AAC and
muxed with tools/mux.swift, so the video is not re-encoded.
"""
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SOUNDS = Path("~/Documents/GitHub/nesso-assets/mixkit").expanduser()
MUX_SRC, MUX = ROOT / "tools/mux.swift", ROOT / "tools/.mux"
RATE = 44100
_cache = {}


def load(name):
    if name not in _cache:
        with wave.open(str(SOUNDS / f"{name}.wav")) as w:
            data = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
            _cache[name] = data.reshape(-1, w.getnchannels())
    return _cache[name]


def fade(x, fin, fout):
    n = len(x)
    a, b = min(n, int(fin * RATE)), min(n, int(fout * RATE))
    if a:
        x[:a] *= np.linspace(0, 1, a)[:, None]
    if b:
        x[n - b:] *= np.linspace(1, 0, b)[:, None]
    return x


def mix(seconds, music=None, music_gain=0.3, music_start=0.0, events=()):
    """events: (time s, sound name, gain, length s or None, offset s into the sound)."""
    n = int(seconds * RATE)
    out = np.zeros((n, 2), dtype=np.float32)
    if music:
        m = load(music)[int(music_start * RATE):]
        m = m[:n].copy() if len(m) >= n else np.concatenate([m] * (n // len(m) + 1))[:n].copy()
        out += fade(m, 0.4, 1.0) * music_gain
    for t, name, gain, length, offset in events:
        s = load(name)[int(offset * RATE):]
        if length:
            s = fade(s[: int(length * RATE)].copy(), 0.02, 0.08)
        start = int(t * RATE)
        if start >= n:
            continue
        end = min(n, start + len(s))
        out[start:end] += s[: end - start] * gain
    peak = np.abs(out).max() or 1
    if peak > 0.89:
        out *= 0.89 / peak
    return out


def mux(video, samples):
    if not MUX.exists():
        subprocess.run(["swiftc", "-O", "-o", str(MUX), str(MUX_SRC)], check=True)
    tmp = Path(tempfile.mkdtemp())
    try:
        wav, m4a, muxed = tmp / "a.wav", tmp / "a.m4a", tmp / "out.mp4"
        with wave.open(str(wav), "wb") as w:
            w.setnchannels(2)
            w.setsampwidth(2)
            w.setframerate(RATE)
            w.writeframes((np.clip(samples, -1, 1) * 32767).astype(np.int16).tobytes())
        subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "160000", str(wav), str(m4a)], check=True)
        subprocess.run([str(MUX), str(video), str(m4a), str(muxed)], check=True)
        shutil.move(str(muxed), str(video))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
