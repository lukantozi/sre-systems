#include <stdio.h>

/* my struggled solution */
void moveZeroes(int *nums, int numsSize) {
    int i, j, tmp;
    for (i = numsSize-1; i >= 0; i--) {
        if (nums[i] == 0) {
            j = i;
            while (j + 1 < numsSize) {
                tmp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = tmp;
                j++;
            }
        }
    }
    /* optimal solution
    int written = 0;
    for (int read = 0; read < numsSize; read++) {
        if (nums[read] != 0) nums[written++] = nums[read];
    }
    while (written < numsSize) {
        nums[written++] = 0;
    }
    */
}

int main(void) {
    int nums[5] = {0,1,0,3,12};
    moveZeroes(nums, 5);
    for (int i = 0; i < 5; i++){
        printf(" %d", nums[i]);
    }
    putchar('\n');
    int nums_a[1] = {0};
    moveZeroes(nums_a, 1);
    printf(" %d", nums_a[0]);
    putchar('\n');
    return 0;
}
