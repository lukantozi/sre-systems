#include <stdio.h>

int main(void) {
    for (int i = 0; i < 5; i++) {
        int i = 999; // hides the i from for loop scope
        printf("%d\n", i); // prints 999 5x
    }
}
