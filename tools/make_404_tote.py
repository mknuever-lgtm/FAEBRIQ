# Builds the 404 tote print: the sticker lockup (Maurice, 2026-09-25: "tote lockup
# spelled out as the sticker version") at 4500px. Serif phrase, six-block bar at
# 1.35x the wordmark, sans FÆBRIQ underneath. Run from the repo root.
import sys; sys.path.insert(0, 'tools')
from PIL import Image
src = open('tools/make_404_v3.py').read().split("build('assets")[0]
v3 = {}; exec(src, v3)
import swap_print_wordmark as sw
OUT = 'assets/print-art/404-straight-not-found-tote-4500.png'
v3['build'](OUT, 4500, True)
sw.swap_sticker(OUT)
