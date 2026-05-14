#include <stdio.h>

int main(void) {
    int a = 12;
    if (a == 12) {
        int b = 99;
        printf("%d, %d\n", a, b); // ok 12, 99
    }
    printf("%d\n", a); // ok, a used inside the scope
    printf("%d\n", b); // not ok, b used outside of the scope
}
