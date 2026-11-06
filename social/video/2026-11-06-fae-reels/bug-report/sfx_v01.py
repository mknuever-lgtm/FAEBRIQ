"""Locally synthesized sound bed for faebriq-bug-report v01. Times in final-video seconds. Usage: python3 -I sfx_v01.py out.wav"""
import math, random, struct, wave, sys
SR = 48000; DUR = 16.0
buf = [0.0] * int(SR * DUR)
random.seed(2069)
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
add(0.0, hit(90), 0.5)
for t in (0.0, 0.4, 0.8): add(t, pop(520), 0.25)
add(2.3, glitch(), 0.22); add(2.42, whoosh(0.3), 0.35)
# issue
add(2.62, tone(220, 0.25, 0.1, sq=True), 0.18)
for i in range(3): add(3.2 + i * 0.45, tone(880, 0.05, 0.02), 0.15)
add(4.75, tone(330, 0.2, 0.08, sq=True), 0.2)
add(5.3, tone(1047, 0.3, 0.12), 0.25)
add(6.1, pop(700), 0.4)
for i in range(3): add(6.9 + i * 0.3, pop(900 + 150 * i), 0.3)
add(8.2, hit(140), 0.75); add(8.2, glitch(), 0.15)
add(9.2, tone(392, 0.25, 0.1), 0.2); add(9.32, tone(262, 0.4, 0.15), 0.2)
# tee + end
add(10.45, whoosh(0.35), 0.4)
add(12.1, hit(110), 0.55); add(11.95, whoosh(0.3), 0.25)
add(13.6, hit(100), 0.6); add(13.6, tone(55, 2.0, 0.7), 0.45)
peak = max(abs(s) for s in buf) or 1
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in buf))
print('peak', round(peak, 3))
