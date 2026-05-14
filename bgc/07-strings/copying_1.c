#include <stdio.h>

int main(void) {
    char s[] = "Hello world";
    int count = 0;
    while (s[count] != '0') {
        count++;
    }
    char t[count+1];
    t[count+1] = '\0';

    while (count != 0) {
        t[count] = s[count];
        count--;
    }

    t[0] = 'j';

    printf("in string s we have %s\n", s);
    printf("in string t we have %s\n", t);
    return 0;
}
