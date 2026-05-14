#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *x;
    if ((x = malloc(sizeof(int) * 10)) == NULL) {
        printf("10 int size allocation failed\n");
    } else printf("address of the x is: %p\n", x);
}
