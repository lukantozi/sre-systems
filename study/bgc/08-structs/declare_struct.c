#include <stdio.h>

struct car {
    char *name;
    float price;
    int speed;
};


int main(void) {
    struct car saturn;
    saturn.name = "Saturn Sl/2";
    saturn.price = 15999.99;
    saturn.speed = 175;

    printf("Name:           %s\n", saturn.name);
    printf("Price (USD):    %f\n", saturn.price);
    printf("Top Speed (km): %d\n", saturn.speed);

    struct car saturn_99 = {"Saturn SL/99", 16000.99, 200};
    printf("Name:           %s\n", saturn_99.name);
    printf("Price (USD):    %f\n", saturn_99.price);
    printf("Top Speed (km): %d\n", saturn_99.speed);

    struct car saturn_01 = {.speed=240, .name="Saturn SL/01"};
    printf("Name:           %s\n", saturn_01.name);
    printf("Price (USD):    %f\n", saturn_01.price);
    printf("Top Speed (km): %d\n", saturn_01.speed);
}
