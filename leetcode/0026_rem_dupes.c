#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *i = nums;
    int k = 1;
    while (i < nums + (numsSize - 1)) {
        if (*i < *(i+1)) nums[k++] = *(i+1);
        i++;
    }
    /* debug
    printf("array: ");
    for (int i = 0; i < numsSize; ++i) {
        printf(" %d", nums[i]);
    }
    putchar('\n');
    printf("length : %d\n\n", k);
    */
    return k;
}

int main(void) { 
    int nums1[10] = {0,0,1,1,1,2,2,3,3,4};
    int size = removeDuplicates(nums1, 10);

    int nums11[2] = {1,1};
    int size11 = removeDuplicates(nums11, 2);

    int nums12[2] = {1,2};
    int size12 = removeDuplicates(nums12, 2);

    int nums13[3] = {1,2,3};
    int size13 = removeDuplicates(nums13, 3);

    int nums111[3] = {1,1,1};
    int size111 = removeDuplicates(nums111, 3);
    return 0;
}
