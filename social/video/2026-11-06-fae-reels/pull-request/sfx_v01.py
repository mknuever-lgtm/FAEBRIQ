"""Locally synthesized sound bed for faebriq-pull-request v01. Times in final-video seconds. Usage: python3 -I sfx_v01.py out.wav"""
import math, random, struct, wave, sys
SR = 48000; DUR = 16.0
buf = [0.0] * int(SR * DUR)
random.seed(1312)
def add(t0, samples, gain=1.0):
    i0 = int(t0 * SR)
    for i, s in enumerate(samples):
        if 0 <= i0 + i < len(buf): buf[i0 + i] += s * gain
def click():
    n = int(0.018 * SR); out = []; prev = 0
    for i in range(n):
        x = random.uniform(-1, 1); prev = 0.6 * prev + 0.4 * x
        out.append((x - prev) * math.exp(-i / (0.003 * SR)))
    return out
def tone(f, d, decay, sq=False):
    out = []
    for i in range(int(d * SR)):
        t = i / SR; s = math.sin(2 * math.pi * f * t)
        if sq: s = (1 if s > 0 else -1) * 0.6
        out.append(s * math.exp(-t / decay) * min(1, i / 48))
    return out
def pop(f=660):  # comment notification: quick pitch-up blip
    out = []
    for i in range(int(0.12 * SR)):
        t = i / SR; ff = f * (1 + 0.6 * min(1, t / 0.03))
        out.append(math.sin(2 * math.pi * ff * t) * math.exp(-t / 0.04) * min(1, i / 48))
    return out
def hit(depth=110):
    out = []
    for i in range(int(0.6 * SR)):
        t = i / SR; f = depth * math.exp(-t * 3) + 45
        out.append(0.9 * math.sin(2 * math.pi * f * t) * math.exp(-t / 0.25))
    return out
def whoosh(d=0.45):
    out = []; lp = 0
    for i in range(int(d * SR)):
        t = i / d / SR; env = math.sin(math.pi * t) ** 2
        a = 0.03 + 0.25 * t; lp = lp + a * (random.uniform(-1, 1) - lp)
        out.append(lp * env * 3)
    return out
def glitch():
    return [random.choice((-1, 1)) * 0.5 * (1 if (i // 120) % 2 else 0) for i in range(int(0.14 * SR))]
def typing(t0, chars, d):
    for k in range(chars): add(t0 + k * d / chars + random.uniform(-0.004, 0.004), click(), random.uniform(0.3, 0.45))

# hook
add(0.0, hit(90), 0.5); add(0.0, pop(520), 0.25); add(0.55, pop(520), 0.25)
add(2.3, glitch(), 0.22); add(2.42, whoosh(0.3), 0.35)
# pull request
for t in (3.35, 4.1, 4.95): add(t, pop(700), 0.4)
add(5.75, hit(140), 0.75); add(5.75, glitch(), 0.15)
add(6.45, whoosh(0.3), 0.3)
# terminal
typing(6.65, 31, 0.65); add(7.35, tone(1320, 0.06, 0.02), 0.15)
typing(7.55, 18, 0.35); add(7.95, tone(1320, 0.06, 0.02), 0.15)
add(8.05, tone(784, 0.25, 0.12), 0.3); add(8.15, tone(1175, 0.4, 0.18), 0.3)
add(8.75, hit(120), 0.7)
for i in range(6): add(9.45 + i * 0.13, tone(440 * 2 ** (i * 2 / 12), 0.09, 0.04), 0.22)
add(10.25, tone(1760, 0.3, 0.12), 0.2); add(10.3, hit(80), 0.45)
# tee + end
add(10.65, whoosh(0.35), 0.4); add(12.15, whoosh(0.3), 0.25)
add(13.6, hit(100), 0.6); add(13.6, tone(55, 2.0, 0.7), 0.45)
peak = max(abs(s) for s in buf) or 1
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in buf))
print('peak', round(peak, 3))
