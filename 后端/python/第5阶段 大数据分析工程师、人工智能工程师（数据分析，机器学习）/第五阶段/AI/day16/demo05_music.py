import json
import numpy as np
import scipy.io.wavfile as wf
with open('../ml_data/12.json', 'r') as f:
    freqs = json.loads(f.read())
tones = [
    ('C1', 0.5),
    ('C2', 0.5),
    ('C3', 0.5),
    ('C4', 0.5),
    ('C5', 0.5),
    ('C6', 0.5),
    ('C7', 0.5),
    ('C8', 0.5),
    
    
    ('G5', 1.5),
    ('A5', 0.5),
    ('G5', 1.5),
    ('E5', 0.5),
    ('D5', 0.5),
    ('E5', 0.25),
    ('D5', 0.25),
    ('C5', 0.5),
    ('A4', 0.5),
    ('C5', 0.75)]
sample_rate = 44100
music = np.empty(shape=1)
for tone, duration in tones:
    times = np.linspace(0, duration, duration * sample_rate)
    sound = np.sin(2 * np.pi * freqs[tone] * times)
    music = np.append(music, sound)
music *= 2 ** 15
music = music.astype(np.int16)
wf.write('music.wav', sample_rate, music)