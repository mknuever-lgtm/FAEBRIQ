# FÆ videos, 2026/11/02: how to rebuild

Edit sources for four videos made with AI Video Studio v0.1.0-beta.6 (github.com/mattp68/ai-video-studio, tag v0.1.0-beta.6). Rendered MP4s and raw clips are NOT in git (too big). Nothing here was published.

| Video | Length | Composition | Sound script |
|---|---|---|---|
| faebriq-404-teaser-v01.mp4 | 15.0s | compositions/comp-v01.html | sound/sfx_v01.py |
| faebriq-404-teaser-v02.mp4 | 16.5s | compositions/comp-v02.html | sound/sfx_v02.py |
| faebriq-zero-results-v01.mp4 | 14.9s | compositions/comp-v03.html | sound/sfx_v03.py |
| faebriq-load-bearing-thread-v01.mp4 | 14.9s | compositions/comp-thread-v01.html | none |
| faebriq-pride-ends-v01.mp4 | 17.4s | compositions/comp-pride-v01.html | sound/sfx_pride_v01.py |

## Raw sources (keep these yourself; hashes in raw-sources.sha256)

- `1311c369-...mp4`: needle + "Something is coming" + eye macro, 1080x1920, 15s
- `2bd24420-F__turnaround_silent.mp4`: FÆ turnaround, 720x1280, 10s, silent
- `67265c93-fae-voice-edit.mp3`: FÆ voice, 84s (transcript: voice-transcript-words.json)
- Also uploaded, unused: `fbecadea-...mp4`, `4171407e-...mp4`, `0213555a-fae.mp4`, `3acf0211-gemini_generated_video_30b40d59.mp4` (fake wordmark tee or wrong bar in several)

## Composition assets

Each composition expects an `assets/` folder next to it, named as below:

- `gsap.min.js`: from the studio's `examples/studio-check/assets/`
- `JetBrainsMono-Regular.ttf`, `JetBrainsMono-Bold.ttf`, `Inter-Medium.otf`, `Inter-SemiBold.otf`: system font files (OFL)
- `wordmark.png`: `assets/print-art/cap-wordmark-slim.png` (locked sans wordmark, six-block bar)
- `tee-model.jpg`: `imagery/shopify/F-BRIQ-404-Straight-Not-Found-Tee-gallery-2-2026-10-10.jpg`
- `tee-flat.jpg`: `imagery/shopify/F-BRIQ-404-Straight-Not-Found-Tee.jpg`
- `p/1.jpg` to `p/10.jpg` (thread; pride uses 1 to 6), all from `imagery/shopify/`:
  1 404 Tee, 2 Code-It-Serve-It Tee, 3 Deploying-Identity Tee, 4 It-s-Not-A-Bug Tee, 5 Off-The-Clock Tee, 6 Please-Hold Tee, 7 Deploying-Identity Heavyweight-Crewnec, 8 Off-The-Clock Heavyweight-Hood, 9 Circuit-Cap-Low-Profile-Black, 10 404 Canvas-Tote

Render: `python3 scripts/hf.py render <folder> --workers 1 --fps 24 --crf 18 --output <out.mp4>` from the studio root. Sound: `python3 -I sound/<script>.py <out.wav>`.

## Assembly (ffmpeg), per video

All: x264 crf 18, yuv420p, AAC 192k, loudnorm I=-14 TP=-1.5, 24fps, 1080x1920. Voice = the mp3; times in seconds.

**404 teaser v02:** 1311 [0, 4] then graphics (12.5s). Clip audio fades out 3.5-4. Voice 34.30-36.85 at 6.36; 37.35-40.25 at 9.30 (voice x1.6, sfx x0.7). v01 is the same without voice, graphics 11s.

**Zero results v01:** turnaround [4.8, 7.2] scaled to 1080x1920 with drawtext captions "FÆ searched your" (from 0.25) / "entire wardrobe." (from 1.0), JetBrains Mono Bold 70 at y 1330/1420; then graphics (12.5s). Voice 77.85-79.95 at 0.2; 80.45-84.05 at 4.4.

**Load-bearing thread v01:** 1311 [2.45, 4.40], [7.40, 8.55], [8.55, 8.98] slowed 2.5x; turnaround [4.8, 9.0]; then montage (6.5s). Captions (Mono Bold 56, y 1440): "FÆ is stitched together" 0.05-1.55, "with queer thread and spite." 1.55-3.3, "The thread is load-bearing." 3.45-5.0, "Ask it about stitch density." 5.15-6.95, "It has opinions." 7.05-8.375. Voice: 21.45-24.70 at 0; 25.62-27.10 at 3.45; 27.50-29.22 at 5.15; 29.90-31.17 at 7.05; 31.98-32.60 at 8.60; 33.05-34.06 at 9.55.

**Pride ends v01:** graphics run full length (17.4s); overlay turnaround [0, 2.85] at 0-2.85 and 1311 [3.45, 4.85] at 5.0-6.4. Captions from captions/pride (index.txt = file|start|end; Mono Bold 58, y 1500). Voice: 6.55-9.20 at 0.15; 9.70-10.30 at 3.25; 11.05-11.95 at 5.15; 14.40-17.15 at 6.6; 72.65-75.09 at 9.6; 75.10-75.80 at 12.3; 76.20-76.92 at 13.3.

Every voice piece: 20 ms fade in, 50 ms fade out.

## Known issues

- Voice file says crewneck $64, hoodie $70, tee $36 (live: $42 / $54 / $32 USD). Never use those lines.
- Voice file reads a stage direction aloud at ~66-72s.
- No mix has been checked by ear.
