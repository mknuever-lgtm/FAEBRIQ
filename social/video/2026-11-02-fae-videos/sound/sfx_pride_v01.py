"""Synthesize the pride v01 sound bed. Times are in final-video seconds."""
import math, random, struct, wave, sys
SR = 48000; DUR = 17.4
buf = [0.0] * int(SR * DUR)
random.seed(404)
def add(t0, samples, gain=1.0):
    i0 = int(t0 * SR)
    for i, s in enumerate(samples):
        if 0 <= i0 + i < len(buf): buf[i0 + i] += s * gain
def click(): # key click: filtered noise burst
    n = int(0.018 * SR); out = []; prev = 0
    for i in range(n):
        x = random.uniform(-1, 1); prev = 0.6 * prev + 0.4 * x
        out.append((x - prev) * math.exp(-i / (0.003 * SR)))
    return out
def tone(f, d, decay, wave_='sine'):
    out = []
    for i in range(int(d * SR)):
        t = i / SR; ph = 2 * math.pi * f * t
        s = math.sin(ph) if wave_ == 'sine' else (1 if math.sin(ph) > 0 else -1) * 0.6
        out.append(s * math.exp(-t / decay) * min(1, i / 48))
    return out
def hit(): # error hit: low sine drop + square buzz
    out = []
    for i in range(int(0.6 * SR)):
        t = i / SR; f = 110 * math.exp(-t * 3) + 45
        out.append(0.9 * math.sin(2 * math.pi * f * t) * math.exp(-t / 0.25))
    buzz = tone(98, 0.35, 0.12, 'square')
    return [a + 0.35 * (buzz[i] if i < len(buzz) else 0) for i, a in enumerate(out)]
def whoosh(d=0.45):
    out = []; lp = 0
    for i in range(int(d * SR)):
        t = i / d / SR; env = math.sin(math.pi * t) ** 2
        a = 0.03 + 0.25 * t; lp = lp + a * (random.uniform(-1, 1) - lp)
        out.append(lp * env * 3)
    return out
def glitch():
    return [random.choice((-1, 1)) * 0.5 * (1 if (i // 120) % 2 else 0) for i in range(int(0.12 * SR))]
def rip():
    out = []; lp = 0
    for i in range(int(0.35 * SR)):
        t = i / SR; lp = lp + 0.5 * (random.uniform(-1, 1) - lp)
        crackle = 1 if random.random() < 0.3 else 0.3
        out.append(lp * crackle * math.exp(-t / 0.12))
    return out
add(3.45, rip(), 0.7)
add(3.5, whoosh(0.35), 0.3)
for i in range(6): add(6.95 + i * 0.11, tone(1046 * (1.12 ** i), 0.06, 0.025), 0.12)
for i in range(11): add(7.7 + i * 0.165, click(), 0.55)
add(10.55, tone(220, 0.5, 0.25), 0.15)
add(11.0, glitch(), 0.3)
add(11.32, tone(880, 0.12, 0.05), 0.2)
add(12.0, whoosh(0.3), 0.3)
add(13.9, [s for s in hit()[: int(0.9 * SR)]], 0.6)
add(13.9, tone(55, 1.6, 0.6), 0.45)
peak = max(abs(s) for s in buf) or 1
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in buf))
print('peak', peak)
