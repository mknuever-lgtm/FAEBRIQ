"""Sound for faebriq-please-hold v01: Kokoro voice lines (telephone EQ), synthesized hold music
(Greensleeves, traditional, public domain), DTMF keys, SIT tones and hits. Usage:
python3 -I mix_v01.py <voice_dir> <out.wav>"""
import math, random, struct, wave, sys
SR = 48000; DUR = 19.5
voice = [0.0] * int(SR * DUR); fx = [0.0] * int(SR * DUR); music = [0.0] * int(SR * DUR)
random.seed(404)
def add(buf, t0, samples, gain=1.0):
    i0 = int(t0 * SR)
    for i, s in enumerate(samples):
        if 0 <= i0 + i < len(buf): buf[i0 + i] += s * gain
def load(path):
    with wave.open(path) as w:
        sr = w.getframerate(); n = w.getnframes(); ch = w.getnchannels(); sw = w.getsampwidth()
        raw = w.readframes(n)
    if sw == 2: x = [v / 32768 for v in struct.unpack('<%dh' % (n * ch), raw)][::ch]
    else:
        import array; x = list(array.array('f', raw))[::ch]
    out = []; step = sr / SR; t = 0.0
    while t < len(x) - 1:
        i = int(t); f = t - i; out.append(x[i] * (1 - f) + x[i + 1] * f); t += step
    return out
def phone(x):  # gentle band-pass (approx 250 Hz - 4 kHz) for an IVR feel
    hp = []; prev_x = prev_y = 0.0; a = math.exp(-2 * math.pi * 250 / SR)
    for v in x: y = a * (prev_y + v - prev_x); hp.append(y); prev_x, prev_y = v, y
    lp = []; y = 0.0; b = 1 - math.exp(-2 * math.pi * 4000 / SR)
    for v in hp: y += b * (v - y); lp.append(y)
    return lp
def tone(f, d, decay=None, amp=1.0):
    out = []
    for i in range(int(d * SR)):
        t = i / SR; env = math.exp(-t / decay) if decay else 1.0
        fade = min(1, i / 240, (int(d * SR) - i) / 240)
        out.append(amp * math.sin(2 * math.pi * f * t) * env * fade)
    return out
def dtmf(key, d=0.16):
    pairs = {'1': (697, 1209), '2': (697, 1336), '3': (697, 1477)}
    a, b = pairs[key]; x = tone(a, d); y = tone(b, d)
    return [0.5 * (p + q) for p, q in zip(x, y)]
def hit(depth=110):
    return [0.9 * math.sin(2 * math.pi * (depth * math.exp(-i / SR * 3) + 45) * i / SR) * math.exp(-i / SR / 0.25) for i in range(int(0.6 * SR))]
def whoosh(d=0.35):
    out = []; lp = 0
    for i in range(int(d * SR)):
        t = i / d / SR; env = math.sin(math.pi * t) ** 2; a = 0.03 + 0.25 * t
        lp = lp + a * (random.uniform(-1, 1) - lp); out.append(lp * env * 3)
    return out
def note(f, d):  # music-box / cheap hold-music organ
    out = []
    for i in range(int(d * SR)):
        t = i / SR; env = math.exp(-t / 0.45) * min(1, i / 120)
        s = math.sin(2 * math.pi * f * t) + 0.35 * math.sin(4 * math.pi * f * t) + 0.12 * math.sin(6 * math.pi * f * t)
        out.append(0.4 * s * env)
    return out

# voice lines: (file, start)
V = [('l1', 0.15), ('l2', 2.25), ('l3', 4.1), ('l4', 6.25), ('l5', 8.5), ('l6', 11.1), ('l7', 14.2), ('l8', 17.0)]
for name, t in V: add(voice, t, phone(load(f'{sys.argv[1]}/{name}.wav')), 1.0)

# hold music 3.4 - 14.1: Greensleeves opening, 3/4 at ~150 bpm, A minor
N = {'A3': 220, 'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.0, 'G#3': 207.65, 'A4': 440.0, 'B3': 246.94, 'E3': 164.81}
beat = 0.4
mel = [('A3', 1), ('C4', 2), ('D4', 1), ('E4', 1.5), ('F4', 0.5), ('E4', 1), ('D4', 2), ('B3', 1), ('G4', 1.5), ('A4', 0.5), ('G4', 1), ('E4', 2), ('C4', 1),
       ('D4', 1.5), ('E4', 0.5), ('D4', 1), ('C4', 2), ('A3', 1), ('G#3', 1.5), ('F4', 0.5), ('G#3', 1), ('A3', 3)]
t = 3.45
while t < 14.0:
    for n, b in mel:
        if t >= 14.0: break
        add(music, t, note(N[n], b * beat + 0.3)); add(music, t, note(N[n] / 2, b * beat + 0.3), 0.35); t += b * beat
for i in range(len(music)):  # fade in/out
    s = i / SR; music[i] *= min(1, max(0, (s - 3.4) / 0.3)) * min(1, max(0, (14.1 - s) / 0.4))
music = phone(music)

# fx
add(fx, 0.0, hit(90), 0.45)
add(fx, 3.3, whoosh(0.3), 0.3)
add(fx, 6.05, dtmf('1'), 0.35); add(fx, 6.2, hit(150), 0.35)
add(fx, 10.2, dtmf('2'), 0.35)
for k, f in enumerate((913.8, 1370.6, 1776.7)): add(fx, 10.3 + k * 0.27, tone(f, 0.26), 0.22)  # special information tones
add(fx, 13.85, dtmf('3'), 0.35)
add(fx, 13.75, whoosh(0.3), 0.25)
add(fx, 15.55, whoosh(0.3), 0.2)
add(fx, 16.8, hit(100), 0.5); add(fx, 16.8, tone(55, 2.2, 0.7), 0.4)

# duck music under voice
env = [0.0] * len(voice); e = 0.0
for i, v in enumerate(voice):
    e = max(abs(v), e * 0.9995); env[i] = e
mix = []
for i in range(len(voice)):
    duck = 1 - min(0.6, env[i] * 4)
    mix.append(voice[i] * 1.0 + music[i] * 0.22 * duck + fx[i])
peak = max(abs(s) for s in mix) or 1
with wave.open(sys.argv[2], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in mix))
print('peak', round(peak, 3))
