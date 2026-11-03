"""Synthesize the v03 sound bed for the zero-results cut. Times are in final-video seconds."""
import math, random, struct, wave, sys
SR = 48000; DUR = 14.9
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
G = 2.4  # graphics start
cmd = 26
for k in range(cmd): add(G + 0.05 + k * 0.5 / cmd + random.uniform(-0.005, 0.005), click(), random.uniform(0.3, 0.45))
for i in range(5): add(G + 0.65 + i * 0.25, tone(880, 0.05, 0.02), 0.12)
add(G + 2.0, tone(1320, 0.08, 0.03), 0.15)
add(G + 2.15, hit(), 0.55)
add(G + 2.33, glitch(), 0.2)
add(G + 3.77, tone(70, 0.3, 0.1), 0.45)
add(G + 4.93, tone(60, 0.35, 0.12), 0.5)
add(G + 5.85, whoosh(0.4), 0.4)
add(G + 7.5, whoosh(0.3), 0.25)
add(G + 9.0, [s for s in hit()[: int(0.9 * SR)]], 0.7)
add(G + 9.0, tone(55, 1.6, 0.6), 0.5)
peak = max(abs(s) for s in buf) or 1
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in buf))
print('peak', peak)
