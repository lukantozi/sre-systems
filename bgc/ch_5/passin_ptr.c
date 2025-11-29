#include <stdio.h>

int increment(int *p) {
    ++*p; // same as *p = *p + 1; (*p++ does not work because ++ operates first;)
}

int main(void) {
    int i = 10;
    int *j = &i;

    printf("i is %d\n", i);
    printf("%p points to value %d\n", j, *j);

    increment(j);

    printf("i now is %d\n", i);
    return 0;
}
