# Your identity put you on hold

Current: V01 ready for review (exports/faebriq-please-hold-v01.mp4, 19.5s, 1080x1920, 24fps, AAC, -14 LUFS). Not approved. Not published.

Structure:
- 0-3.4s: FÆ still push-in. "incoming call · you → your identity". VO: "Thank you for calling your identity." (0.15) "Please hold." (2.25, big text).
- 3.4-14.1s: IVR screen, ON HOLD, timer, "now playing: greensleeves.mid", EQ bars. Menu: [1] explain yourself (VO 4.1, press 6.05, DISCONTINUED, VO "That option has been discontinued." 6.25); [2] the old you (VO 8.5, press 10.2, SIT tones 10.3, NOT IN SERVICE, VO "The number you have reached is no longer in service." 11.1); [3] wear the rebrand (12.6, press 13.85). Captions mirror VO.
- 14.1-16.8s: Please Hold tee on-model, VO "Your rebrand is ready." (14.2); flat front with "$32 USD · ships US + Canada".
- 16.8-19.5s: wordmark + six-block bar, VO + text "Thank you for holding.", faebriq.com.

Voice: Kokoro-82M int8 ONNX (Apache 2.0, local, free), voice af_heart, speed 0.95. Model files from github.com/thewh1teagle/kokoro-onnx release model-files-v1.0: kokoro-v1.0.int8.onnx sha256 6e742170d309016e5891a994e1ce1559c702a2ccd0075e67ef7157974f6406cb, voices-v1.0.bin sha256 bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d. Script: work/tts_v01.py. Lines: audio/voice/l1-l8.wav. This is a synthetic voice, not FÆ's recorded voice.
Music: Greensleeves (traditional, public domain), synthesized in work/mix_v01.py, telephone EQ, ducked under VO.
Build: graphics via scripts/hf.py render (24fps crf 18); `python3 -I work/mix_v01.py audio/voice work/mix-v01.wav`; mux x264 crf 18, AAC 192k, loudnorm I=-14 TP=-1.5.
Checks: each VO line and the final mix transcribed back with local faster-whisper small (int8); all eight lines read correctly after moving a whoosh off line 7. Assistant cannot listen: tone, warmth and music balance unreviewed by ear.
