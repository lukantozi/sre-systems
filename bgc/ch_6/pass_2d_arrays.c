#include <stdio.h>

void print_2D_array(int a[][3]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}

int main(void) {
    int x[2][3] = {
        {3, 4, 5},
        {2, 6, 1}
    };
    print_2D_array(x);
}
