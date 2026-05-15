#include <stdio.h>
#include <float.h>

int main(void) {
    float f = 3.14159f;
    float g = 0.00000265358f;

    printf("%.5f\n", f);
    printf("%.11f\n", g);

    f += g;
    printf("%.11f\n", f);
}
