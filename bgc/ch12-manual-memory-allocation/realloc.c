#include <stdio.h>
#include <stdlib.h>


int main(void) {
    float *pf = malloc(sizeof(float)*20);
    for (int i = 0; i < 20; i++) {
        *(pf+i) = (i%43)*0.2 * i;
    }
    float *pfn = realloc(pf, sizeof(float)*40);
    if (pfn == NULL) {
        printf("Reallocation failed\n");
        free(pf);
        return 1;
    }
    pf = pfn;
    for (int i = 20; i < 40; i++) {
        *(pf+i) = (i%43)*0.2 * i;
    }
    for (int i = 0; i < 40; i++) {
        printf("%f\n", pf[i]);
    }
    free(pf);
}
