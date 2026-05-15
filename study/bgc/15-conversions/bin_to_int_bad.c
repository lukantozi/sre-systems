#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *s = "34x90";
    char *badchar;

    unsigned long int x = strtoul(s, &badchar, 10);

    if (*badchar == '\0') {
        printf("Success! %lu\n", x);
    } else {
        printf("Managed to convert partially: %lu\n", x);
        printf("Invalid character: %c\n", *badchar);
    }
}
