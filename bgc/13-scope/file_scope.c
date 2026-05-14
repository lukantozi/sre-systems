#include <stdio.h>

int shared = 10; // visible to all functions

void func1(void) {
    shared += 100; // shared now is 110
}

void func2(void) {
    printf("%d\n", shared); // prints 110
}

int main(void) {
    func1();
    func2();
}
