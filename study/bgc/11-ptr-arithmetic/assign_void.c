#include <stdio.h>

int main(void) {
    char a = 'X';
    void *p = &a;
    char *c = p;
    //printf("%c", *p); can't dereference void
    printf("%c\n", *c);
}
