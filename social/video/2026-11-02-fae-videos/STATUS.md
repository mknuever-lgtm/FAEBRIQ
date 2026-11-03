# FAEBRIQ 404 teaser

Current: V01 ready for review (exports/faebriq-404-teaser-v01.mp4, 15s, 1080x1920, 24fps). Not approved. Not published.

Structure:
- 0-4s: raw/1311c369 clip 0.0-4.0 (needle, "Something is coming.", FAE eye close-up). Clip audio kept, faded out 3.5-4.0.
- 4-8s: terminal "> searching for: straight..." then 404 / STRAIGHT NOT FOUND.
- 8-11.5s: real Shopify 404 tee images (on-model, then flat), "$32 USD, ships US + Canada".
- 11.5-15s: locked sans wordmark with six-block bar (assets/print-art/cap-wordmark-slim.png), "Wear the glitch.", faebriq.com.

Build: work/comp-v01/index.html rendered via scripts/hf.py render (24fps, crf 18); sound: work/scripts/sfx_v01.py (locally synthesized); mix loudnorm -14 LUFS.

Limits: assistant cannot listen to audio. Clip audio and SFX mix unreviewed by ear. Voice track raw/67265c93-fae-voice-edit.mp3 unused: no transcription available in this environment (model downloads blocked).
Excluded on purpose: clips showing the fake wordmark tee and non-locked bars.

## V02 (2026-11-02)
exports/faebriq-404-teaser-v02.mp4, 16.5s. Not approved. Not published.
Adds FAE voice from raw/67265c93-fae-voice-edit.mp3: 34.30-36.85 ("404. Straight, not found.") placed at 6.36s so "404" lands on the 404 hit; 37.35-40.25 ("Error is permanent. Do not refresh.") at 9.30s with burned-in captions. Terminal held 1s longer, tee and end card shifted.
Transcript: work/voice-transcript-words.json (faster-whisper small int8, local; model from npm @skillninja/shortmovie-telop-model p0-p3, sha256 verified).
Voice file issues (not used in this cut): states crewneck $64, hoodie $70, tee $36 (live: $42/$54/$32); reads a stage direction aloud at ~66-72s; "FAEBRIQ" at ~12.6s transcribed as "Fave Rick Hick" (pronunciation unverified).

## Zero results cut V01 (2026-11-02)
exports/faebriq-zero-results-v01.mp4, 14.9s. Not approved. Not published.
0-2.4s raw/2bd24420 turnaround 4.8-7.2 with captions; voice 77.85-79.95 at 0.2s. Graphics work/comp-v03 from 2.4s: wardrobe scan, "0 RESULTS" on voice 80.45-84.05 placed at 4.4s, tee with "1 patch available." / "> install 404", end card. SFX work/scripts/sfx_v03.py.

## Load-bearing thread V01 (2026-11-02)
exports/faebriq-load-bearing-thread-v01.mp4, 14.9s. Not approved. Not published. Footage: 1311 2.45-4.40, 7.40-8.55, 8.55-8.98 slowed 2.5x; turnaround 4.8-9.0. Voice 21.45-34.06 in six pieces. Montage work/comp-thread-v01: 10 live products (6 tees, crewneck, hoodie, Low Profile cap, Canvas Tote), end card. No SFX.

## Pride ends V01 (2026-11-02)
exports/faebriq-pride-ends-v01.mp4, 17.4s. Not approved. Not published. Footage: turnaround 0-2.85, 1311 3.45-4.85. Graphics work/comp-pride-v01 (calendar rip, re-stitch, month flips, grey-out glitch, 6 tees, end card). Voice: 6.55-9.20, 9.70-10.30, 11.05-11.95, 14.40-17.15, 72.65-75.09, 75.10-75.80, 76.20-76.92. SFX work/scripts/sfx_pride_v01.py. Captions work/captions-pride.
