#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int)); //sizeof *p -> will work too because, constant expression *p evaluates to int type
    *p = 12;
    printf("%d\n", *p);
    free(p);
}
