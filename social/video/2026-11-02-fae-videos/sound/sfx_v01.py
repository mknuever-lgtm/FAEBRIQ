"""Synthesize the v01 sound bed for the 404 teaser. Times are in final-video seconds."""
import math, random, struct, wave, sys
SR = 48000; DUR = 15.0
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
G = 4.0  # graphics start
typed = 25; t0 = G + 0.2; dt = 1.3 / typed
for k in range(typed): add(t0 + k * dt + random.uniform(-0.01, 0.01), click(), random.uniform(0.35, 0.55))
for t in (1.75, 2.0, 2.25): add(G + t, tone(1320, 0.07, 0.03), 0.18)
add(G + 2.6, hit(), 0.9)
add(G + 2.78, glitch(), 0.25)
add(G + 3.05, tone(660, 0.12, 0.05, 'square'), 0.12)
add(G + 3.85, whoosh(0.4), 0.5)
add(G + 5.9, whoosh(0.3), 0.35)
add(G + 7.5, [s * 1.0 for s in hit()[: int(0.9 * SR)]], 0.7)
add(G + 7.5, tone(55, 1.6, 0.6), 0.5)
peak = max(abs(s) for s in buf) or 1
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in buf))
print('peak', peak)
