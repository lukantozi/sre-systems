#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *s = "101010";

    unsigned long int x = strtoul(s, NULL, 2);
    printf("%lu\n", x);
}
