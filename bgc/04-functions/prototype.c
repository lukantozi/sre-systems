#include <stdio.h>

int foo(void);


int main(void) {
    int i = foo();

    printf("i = %d\n", i);
}


int foo(void) {
    return 3490;
}
