#!/bin/bash
set -e
OBJ=object_input.png
HOLO=holo_demo.png
OUTDIR=demo_multi_z
if [ ! -f $HOLO ]; then
    echo "Using precomputed hologram holo_demo.png"
fi
python3 recon_multi_z.py $HOLO --zs 0.02 0.04 0.06 0.08 --outdir $OUTDIR --unwrap
echo "Demo complete. Check $OUTDIR for outputs."
