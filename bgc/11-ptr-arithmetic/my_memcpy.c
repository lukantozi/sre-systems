#include <stdio.h>

void *my_memcpy(void *dest, void *src, int bytecount) {
    char *d = dest;
    char *s =  src;

    while (bytecount--) {
        *d++ = *s++;
    }

    return dest; // not necessary, useful sometimes
}

int main(void) {
    char s[] = "To copy";
    char b[100];

    my_memcpy(b, s, 8);

    printf("%s\n", b);
}
