#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = calloc(10, sizeof(int));
    for (int i = 0; i < 10; i++) {
        printf("%p\n", &p[i]);
    }
    free(p);
    printf("\n");
    int *p1 = malloc(sizeof(int)*10);
    for (int i = 0; i < 10; i++) {
        printf("%p\n", &p1[i]);
    }
    free(p1);
}
