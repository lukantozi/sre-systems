#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int)*10);
    // assign values 0-45
    for (int i = 0; i < 10; i++) {
        p[i] = i*5;
    }
    // print the values 0, 5, ... , 40, 45
    for (int i = 0; i < 10; i++) {
        printf("%d\n", p[i]);
    }
    free(p);
}
