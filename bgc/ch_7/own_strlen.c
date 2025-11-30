#include <stdio.h>

int main(void) {
    char *s = "Hello world";

    int count = 0;

    while (s[count] != '\0') {
        count++;
    }
    printf("String's length is %d\n", count);
    return 0;
}
