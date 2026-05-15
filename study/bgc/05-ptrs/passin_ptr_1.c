#include <stdio.h>

int increment(int *p) {
    ++*p;
}

int main(void) {
    int i = 10;
    printf("i is %d\n", i);
    increment(&i);
    printf("i is %d\n", i);
    return 0;
}
