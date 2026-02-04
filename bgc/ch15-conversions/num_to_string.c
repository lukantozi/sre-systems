#include <stdio.h>

int main(void) {
    char s[10];
    float f = 3.14159;

    snprintf(s, 10, "%f", f);
    printf("%s\n", s);
}
