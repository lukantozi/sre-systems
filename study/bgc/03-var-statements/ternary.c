#include <stdio.h>

int main(void) {
    int y = 0;
    int x = 14;
    y += x > 10? 17: 37;
    printf("The number is %d\n", y);

    y = 0;
    x = 4;
    if (x > 10) {
        y += 17;
    } else {
        y += 37;
    }
    printf("The number is %d\n", y);
}
