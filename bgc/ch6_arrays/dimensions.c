#include <stdio.h>

int main(void) {
    int row, col;

    int a[2][5] = {
        {0, 2, 4, 12, 23},
        {34, 94, 123, 59, 2}
    };

    for (row = 0; row < 2; row++) {
        for (col = 0; col < 5; col++) {
            printf("(%d,%d) = %d\n", row+1, col+1, a[row][col]);
        }
    }
    printf("\n");
    int b[3][3] = {[0][0]=1, [1][1]=1, [2][2]=1};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }
    return 0;
}
