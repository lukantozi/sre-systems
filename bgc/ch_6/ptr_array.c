#include <stdio.h>

int main(void) {
    int a[5] = {11, 23, 56, 2, 6};
    int *p;

    p = &a[0];
    int *t = &a[1];
    int *pt = a;


    printf("%d\n", *p);
    printf("%d\n", *t);
    printf("%d\n", *(p+1));
    printf("%d\n", *(p+2));
    printf("%d\n", *(p+3));
    return 0;
}
