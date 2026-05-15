#include <stdio.h>

int removeElement(int* nums, int numsSize, int val) {
    /* struggle
    if (numsSize == 0) return 0;
    int k = 0;
    int l = numsSize - 1;
    int count = numsSize;
    int tmp;
    while (k <= l && l >= 0) {
        if (nums[k] != val) k++;
        else {
            while (k <= l && l >= 0) {
                if (val == nums[l]) l--;
                else {
                    tmp = nums[k];
                    nums[k++] = nums[l];
                    nums[l--] = tmp;
                    break;
                }
           } 
        }
    }
    */

    /* Solution */
    int k = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) nums[k++] = nums[i];
    }

    /* debug
    printf("k: %d, Value: %d\n", k, val);
    printf("list: ");
    for (int i = 0; i < numsSize; i++) {
        printf(" %d", nums[i]);
    }
    putchar('\n');
    putchar('\n');
    */
     
    return k;
}

int main(void) {
    int nums3[4] = {3,2,2,3};
    int size3 = removeElement(nums3, 4, 3);

    int nums2[8] = {0,1,2,2,3,0,4,2};
    int size2 = removeElement(nums2, 8, 2);

    int nums1[1] = {1};
    int size1 = removeElement(nums1, 1, 1);

    int nums11[2] = {1, 1};
    int size11 = removeElement(nums11, 2, 1);

    int nums33[2] = {3,3};
    int size33 = removeElement(nums33, 2, 3);

    int nums23[1] = {2};
    int size23 = removeElement(nums23, 1, 3);

    int nums423[4] = {1,2,3,4};
    int size423= removeElement(nums423, 4, 1);
}
