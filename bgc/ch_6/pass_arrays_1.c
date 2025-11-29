#include <stdio.h>

void double_array(int *a, int len) {
    for (int i = 0; i < len; i++) {
        a[i] *= 2;
    }
}

int main(void) {
    int x[5] = {2, 4, 5, 6, 10};

    double_array(x, 5);

    for (int i = 0; i < 5; i++) {
        printf("%d\n", x[i]);
    }
    return 0;
}
