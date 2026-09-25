#!/usr/bin/env bash
# Rebuild the on-model product shots with the real print masters composited on.
#
# The generated model photos have good lighting and drape but their prints are
# invented: wrong artwork, a smooth gradient instead of the six-block pride
# bar, and on the cap a swoosh across the brim that the locked cap spec does
# not have. This re-lays each real master onto the same photo.
#
# The quads were set by eye against each photo. If a source photo is ever
# replaced, re-tune the quad and roi for it; --debug draws both.
#
#   bash tools/make_model_composites.sh
set -euo pipefail
cd "$(dirname "$0")/.."

python3 tools/composite_print.py \
  --garment assets/model-tee-new.png \
  --print   assets/print-art/code-it-serve-it-light-4500.png \
  --quad 310,258,414,256,415,302,311,304 \
  --roi  258,234,436,308 \
  --out  assets/model-tee-print.png

python3 tools/composite_print.py \
  --garment assets/model-hoodie-new.png \
  --print   assets/print-art/deploying-identity-v2-light-4500.png \
  --quad 306,250,416,249,417,285,307,286 \
  --roi  282,226,438,316 \
  --heal-threshold 2.2 \
  --out  assets/model-hoodie-print.png

python3 tools/composite_print.py \
  --garment assets/model-cap-new.png \
  --print   assets/print-art/cap-wordmark-structured.png \
  --quad 240,209,388,214,387,258,239,253 \
  --roi  165,188,412,270 \
  --heal-also 230,282,420,350 \
  --heal-threshold 2.6 \
  --displace 0.5 \
  --out  assets/model-cap-print.png

echo "done: assets/model-{tee,hoodie,cap}-print.png"
