#include <stdio.h>

int main(void) {
    int x = 5;
    char *d = "hello";
    printf("%zu\n", sizeof x);
    printf("%zu\n", sizeof(x + 2));
    printf("%zu\n", sizeof 3.14);
    printf("%zu\n", sizeof *d);
    printf("%zu\n", sizeof(int));
    printf("%zu\n", sizeof(char));
}
