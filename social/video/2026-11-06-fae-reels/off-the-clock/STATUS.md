# Logged off at 5

Current: V02 ready for review (exports/faebriq-off-the-clock-v02.mp4, comp-v02.html, 2026/11/14). Not approved. Not published. Logged in Notion Content Library as Drafts.

V02 (hoodie, per Content OS Launch script 5): same timings, voice and mix (mix-v01.wav) as V01. Hoodie on screen all 18.5s: front hero with FÆ inset (0-3.4), on-model below the terminal (3.4-10.8), on-model lock-screen wallpaper (10.8-13.4), push-in on the front print "Off the clock." then print close-up "Still iconic." with "$54 USD · ships US + Canada" (13.4-16.2), folded hoodie over the wordmark end card (16.2-18.5). Assets: hood-front.jpg (and copy hood-front-b.jpg) = Off-The-Clock-Still-Iconic-Heavyweight-Hood, hood-man.jpg = ...Heavyweight-Hood-gallery-2, hood-woman.jpg = ...Hoodie-gallery-2, hood-close.jpg = ...Heavyweight-Hood-gallery-3, hood-fold.jpg = ...Heavyweight-Hood-gallery-4 (imagery/shopify, scaled to 1536x1920).

V01 below (tee), kept for history.

Script source: SOCIAL_LAUNCH_POSTS_2026-09-23.md post 5 (on-screen text). FÆ's recording has no Off The Clock lines, so FÆ speaks unused lines that fit.

Structure:
- 0-3.4s: FÆ still, clock 16:59 → 17:00, "Logged off at 5." FÆ: "FÆ has a plan." (1.0) "Don't worry about the plan." (2.5)
- 3.4-10.8s: terminal: logout, work session closed 17:00:00; ps aux | grep iconic → "1 running always iconic"; "Did not log off from being iconic."; kill -9 1 → operation not permitted; "That process runs in the background and cannot be killed." FÆ: "Never has." (9.0) "Never will." (9.95)
- 10.8-13.4s: 17:04 lock screen, "manager · #general · quick question" swiped away, "1 unread" pops back. "Pretending you didn't see the Slack notification." FÆ: "The plan is great." (11.6) "Probably." (12.65)
- 13.4-16.2s: Off The Clock tee on-model "Off the clock.", flat "Still iconic.", "$32 USD · ships US + Canada".
- 16.2-18.5s: wordmark + six-block bar, "Runs in the background.", faebriq.com.

Voice clips (audio/voice, 20 ms fade in / 50 ms out) from raw/67265c93-fae-voice-edit.mp3 (sha256 42d74444...ddfc): v1 60.15-61.55, v2 62.30-63.62, v3 63.85-64.75, v4 65.00-65.75, v5 75.05-75.80, v6 76.15-76.95. Avoided: price lines (stale) and the stage direction at ~66-72s.
Build: graphics via scripts/hf.py render (24fps crf 18); `python3 -I work/mix_v01.py audio/voice work/mix-v01.wav`; mux x264 crf 18, AAC 192k, loudnorm I=-14 TP=-1.5.
Checks: clips and final mix transcribed back with local faster-whisper small; all six lines read correctly. Mix not checked by ear.
