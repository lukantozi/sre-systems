#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL));
    int ub = 3;
    int lb = 1;
    int goat_count = rand() % (ub - lb + 1) + lb;

    switch (goat_count) {
        case 0:
            printf("You have no goats\n"); 
            //break; // if you don't break, even if the condition above is true, it will execute the next case (till the break is called)

        case 1:
            printf("You have a single goat\n");
            //break;

        case 2:
            printf("You have two goats\n");
            //break;

        case 3:
            printf("You have three goats\n");
            //break;

        default:
            printf("You have pletora of goats\n");
            break;
    }
    return 0;
}
