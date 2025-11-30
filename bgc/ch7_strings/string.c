#include <stdio.h>

int main(void) {
    char *s = "Hello world";
    char f[] = "Hello world";

    printf("%s\n", s);
    for (int i = 0; i < 13; i++) {
        printf("%c", s[i]);
    }
    printf("\n");
}
