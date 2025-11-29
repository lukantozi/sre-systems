#include <stdio.h>

#define COUNT 5

int main(void) {
    int i;
    int a[COUNT] = {[COUNT-2]=555, 98};

    for (i = 0; i < 10; i++) {
        printf("%d\n", a[i]);
    }
    return 0;
}
