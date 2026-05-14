#include <stdio.h>

int main(void) {
    int i;
    float f[4];

    f[0] = 3.144;
    f[1] = 2.2313;
    f[2] = 4.32;
    f[3] = 5.123;

    for (i = 0; i < 4; i++) {
        printf("f[%d] = %f\n", i, f[i]);
    }
    return 0;
}
