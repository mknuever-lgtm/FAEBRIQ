# FÆ tee reels, 2026/11/03 to 2026/11/06: how to rebuild

Edit sources for four 9:16 reels made with AI Video Studio v0.1.0-beta.6 (github.com/mattp68/ai-video-studio, tag v0.1.0-beta.6). Rendered MP4s, raw media and voice WAVs are NOT in git. Nothing here was published. Each folder's STATUS.md has the shot list, timings and checks.

- pull-request: "FÆ reviewed your coming out", Deploying Identity v2.0 tee, 16.0s, SFX only.
- bug-report: "Someone filed a bug report about you", It's Not A Bug. It's Me. tee, 16.0s, SFX only.
- please-hold: "Your identity put you on hold", Please Hold tee, 19.5s, Kokoro TTS voice + synthesized Greensleeves hold music.
- off-the-clock: "Logged off at 5", 18.5s, FÆ's recorded voice. On-screen script from SOCIAL_LAUNCH_POSTS_2026-09-23.md post 5. V01 = tee (comp-v01.html); V02 = hoodie on screen all 18.5s (comp-v02.html, assets listed in its STATUS.md, same mix as V01).

## Composition assets

Each comp-v01.html expects an `assets/` folder next to it:

- `gsap.min.js`: the studio's `examples/studio-check/assets/gsap.min.js`
- `JetBrainsMono-Regular.ttf`, `JetBrainsMono-Bold.ttf`, `Inter-Medium.otf`, `Inter-SemiBold.otf`: system font files (OFL)
- `fae.jpg`: the clean FÆ still (720x1280 webp from the chat upload) resized to 1080x1920
- `fae-avatar.jpg` (pull-request, bug-report): crop (150,160)-(570,580) of that still, resized to 240x240
- `wordmark.png`: `assets/print-art/cap-wordmark-slim.png`
- Tee photos from `imagery/shopify/`:
  - pull-request: `tee-model.jpg` = Deploying-Identity-v2-0-Tee-gallery-2-2026-10-10, `tee-flat.jpg` = Deploying-Identity-v2-0-Tee
  - bug-report: `tee-model.jpg` = It-s-Not-A-Bug-It-s-Me-Tee-gallery-2, `tee-fold.jpg` = It-s-Not-A-Bug-It-s-Me-Tee-gallery-4
  - please-hold: `tee-model.jpg` = Please-Hold-I-m-Rebranding-My-Identity-Tee-gallery-2, `tee-flat.jpg` = Please-Hold-I-m-Rebranding-My-Identity-Tee
  - off-the-clock: `tee-model.jpg` = Off-The-Clock-Still-Iconic-Tee-gallery-2, `tee-flat.jpg` = Off-The-Clock-Still-Iconic-Tee

## Render and mix (from the studio root)

1. `python3 scripts/hf.py render <folder> --workers 1 --fps 24 --crf 18 --output graphics.mp4`
2. Sound:
   - pull-request, bug-report: `python3 -I sfx_v01.py sfx.wav`
   - please-hold: generate lines with `tts_v01.py <kokoro_dir> <voice_dir>` (kokoro-onnx, model-files-v1.0, hashes in STATUS.md), then `python3 -I mix_v01.py <voice_dir> mix.wav`
   - off-the-clock: cut v1 to v6 from `67265c93-fae-voice-edit.mp3` at the times in STATUS.md (48 kHz mono, 20 ms fade in, 50 ms fade out), then `python3 -I mix_v01.py <voice_dir> mix.wav`
3. Mux: `ffmpeg -i graphics.mp4 -i <sound>.wav -map 0:v -map 1:a -c:v libx264 -crf 18 -pix_fmt yuv420p -r 24 -af loudnorm=I=-14:TP=-1.5 -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart out.mp4`

## Known limits

- No mix has been checked by ear. Voice lines were verified by transcribing them back with local faster-whisper small.
- Prices and shipping copy follow CLAUDE.md as of 2026/11/06: tees $32 USD, ships US + Canada.
