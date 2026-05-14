#include <stdio.h>

int main(void) {
    int a[5] = {11, 22, 33, 44, 55};
    int *p = &a[0]; // int *p = a; also works!
    for (int i = 0; i < 5; i++) {
        printf("%d\n", *(p+i));
    }
}
