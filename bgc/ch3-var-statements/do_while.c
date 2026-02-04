#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int r;

    srand(time(NULL));
    do {
        r = rand() % 100;
        printf("%d\n", r);
    } while (r != 37);
    return 0;
}
