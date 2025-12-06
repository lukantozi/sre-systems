#include <stdio.h>

typedef struct {
    int x, y;
} point;

int main(void) {
    point p = {.x=3, .y=5};
    printf("x = %d\ny = %d\n", p.x, p.y);
}
