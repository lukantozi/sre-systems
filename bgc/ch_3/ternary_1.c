#include <stdio.h>


int main(void) {
    for (int i = 0; i < 10; i++) {
        printf("the number %d is %s\n", i, i % 2 == 0? "Even": "Odd");
    }
    /*
    int x = 1;
    printf("the number %d is %s\n", x, x % 2 == 0? "Even": "Odd");
    x = 2;
    printf("the number %d is %s\n", x, x % 2 == 0? "Even": "Odd");
    */
    return 0;
}
