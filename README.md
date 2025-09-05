~~~
FFT Hologram — v4 (Self-contained, No GPU)
==========================================

This v4 release includes everything to demo FFT holography without GPU.

Contents:
- holo_full.c      : simple C forward hologram generator (writes holo_demo.pgm)
- recon_multi_z.py : multi-z reconstructor with noise injection, phase unwrapping
- recon_adv.py     : single z reconstructor
- depth_demo.sh    : demo runner (uses precomputed holo_demo.png)
- object_input.png : sample object (circle + TEST)
- holo_demo.png    : precomputed hologram (for demo without compiling C)
- README.md        : this file
- VERSION.md       : version log

Quick Start:
------------
1. Run the demo:
   chmod +x depth_demo.sh
   ./depth_demo.sh

2. View outputs in demo_multi_z/

3. To compile the C generator:
   gcc -O2 -o holo_full holo_full.c -lm
   ./holo_full

Dependencies:
   pip3 install numpy imageio matplotlib scikit-image
~~~
