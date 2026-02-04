#include <stdio.h>

int main(void) {
    int i = 10;

    {
        int i = 20;
        printf("%d\n", i); // 20 (inner scope), outer scope is hidden
    }
    printf("%d\n", i); // 10, outer scope i
}
