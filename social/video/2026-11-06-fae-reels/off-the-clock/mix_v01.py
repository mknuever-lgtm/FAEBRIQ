"""Sound for faebriq-off-the-clock v01: FÆ voice clips (audio/voice/v1-v6.wav, cut from raw/67265c93-fae-voice-edit.mp3)
plus locally synthesized SFX. No music. Usage: python3 -I mix_v01.py <voice_dir> <out.wav>"""
import math, random, struct, wave, sys
SR = 48000; DUR = 18.5
voice = [0.0] * int(SR * DUR); fx = [0.0] * int(SR * DUR)
random.seed(1700)
def add(buf, t0, samples, gain=1.0):
    i0 = int(t0 * SR)
    for i, s in enumerate(samples):
        if 0 <= i0 + i < len(buf): buf[i0 + i] += s * gain
def load(path):
    with wave.open(path) as w:
        assert w.getframerate() == SR and w.getsampwidth() == 2
        n = w.getnframes(); return [v / 32768 for v in struct.unpack('<%dh' % n, w.readframes(n))]
def click():
    n = int(0.018 * SR); out = []; prev = 0
    for i in range(n):
        x = random.uniform(-1, 1); prev = 0.6 * prev + 0.4 * x
        out.append((x - prev) * math.exp(-i / (0.003 * SR)))
    return out
def tone(f, d, decay, amp=1.0):
    return [amp * math.sin(2 * math.pi * f * i / SR) * math.exp(-i / SR / decay) * min(1, i / 48) for i in range(int(d * SR))]
def hit(depth=110):
    return [0.9 * math.sin(2 * math.pi * (depth * math.exp(-i / SR * 3) + 45) * i / SR) * math.exp(-i / SR / 0.25) for i in range(int(0.6 * SR))]
def whoosh(d=0.35):
    out = []; lp = 0
    for i in range(int(d * SR)):
        t = i / d / SR; env = math.sin(math.pi * t) ** 2; a = 0.03 + 0.25 * t
        lp = lp + a * (random.uniform(-1, 1) - lp); out.append(lp * env * 3)
    return out
def typing(t0, chars, d):
    for k in range(chars): add(fx, t0 + k * d / chars + random.uniform(-0.004, 0.004), click(), random.uniform(0.3, 0.45))

for name, t in [('v1', 1.0), ('v2', 2.5), ('v5', 9.0), ('v6', 9.95), ('v3', 11.6), ('v4', 12.65)]:
    add(voice, t, load(f'{sys.argv[1]}/{name}.wav'))

add(fx, 0.0, tone(1500, 0.05, 0.015), 0.2)          # clock tick
add(fx, 0.5, tone(880, 0.35, 0.15), 0.25); add(fx, 0.5, tone(1320, 0.35, 0.15), 0.15)  # 17:00 chime
add(fx, 3.3, whoosh(0.3), 0.3)
typing(3.5, 8, 0.3); add(fx, 3.85, tone(1320, 0.06, 0.02), 0.12)
typing(4.4, 22, 0.6); add(fx, 5.05, tone(1320, 0.06, 0.02), 0.12)
add(fx, 5.25, tone(660, 0.1, 0.04), 0.15)
typing(7.6, 11, 0.35); add(fx, 8.0, tone(1320, 0.06, 0.02), 0.12)
add(fx, 8.1, hit(140), 0.6)
add(fx, 10.7, whoosh(0.3), 0.3)
add(fx, 10.9, tone(988, 0.18, 0.08), 0.3); add(fx, 11.02, tone(1319, 0.3, 0.12), 0.3)  # notification
add(fx, 12.0, whoosh(0.28), 0.35)                    # swipe away
add(fx, 12.6, tone(1568, 0.1, 0.04), 0.2)            # unread badge
add(fx, 13.35, whoosh(0.3), 0.3)
add(fx, 14.8, hit(110), 0.45)
add(fx, 16.2, hit(100), 0.55); add(fx, 16.2, tone(55, 2.0, 0.7), 0.4)

mix = [v * 1.0 + f * 0.8 for v, f in zip(voice, fx)]
peak = max(abs(s) for s in mix) or 1
with wave.open(sys.argv[2], 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(s / peak * 0.89 * 32767)) for s in mix))
print('peak', round(peak, 3))
