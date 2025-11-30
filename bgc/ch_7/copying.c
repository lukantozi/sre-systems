#include <stdio.h>

int main(void) {
    char s[] = "Hello world";
    char *t = s;

    t[0] = 'z';

    printf("%s\n", s);
}
