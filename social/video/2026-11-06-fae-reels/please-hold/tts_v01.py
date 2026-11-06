import sys, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro(sys.argv[1] + '/kokoro-v1.0.int8.onnx', sys.argv[1] + '/voices-v1.0.bin')
lines = {
 'l1': "Thank you for calling your identity.",
 'l2': "Please hold.",
 'l3': "To explain yourself, press one.",
 'l4': "That option has been discontinued.",
 'l5': "For the old you, press two.",
 'l6': "The number you have reached is no longer in service.",
 'l7': "Your rebrand is ready.",
 'l8': "Thank you for holding.",
}
for key, text in lines.items():
    a, sr = k.create(text, voice='af_heart', speed=0.95, lang='en-us')
    sf.write(f'{sys.argv[2]}/{key}.wav', a, sr)
    print(key, sr, round(len(a) / sr, 2), text)
