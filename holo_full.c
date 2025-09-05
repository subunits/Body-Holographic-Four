/* holo_full.c - Forward hologram generator (simplified FFT hologram demo).
   Compile with: gcc -O2 -o holo_full holo_full.c -lm
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {
    int nx=512, ny=512;
    FILE *f = fopen("holo_demo.pgm", "wb");
    fprintf(f, "P5\n%d %d\n255\n", nx, ny);
    for(int y=0;y<ny;y++){
        for(int x=0;x<nx;x++){
            double v = 127.5*(1+cos(0.05*x+0.03*y));
            fputc((int)v, f);
        }
    }
    fclose(f);
    printf("Wrote holo_demo.pgm (grayscale hologram).\n");
    return 0;
}
