/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int *result = (int*)malloc((*returnSize) * sizeof(int));
    if (result == NULL) {
        exit(1);
    }
    for (int i = 0; i < numsSize; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if (target - nums[i] == nums[j]) {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    return result;
}


int main(void) {
   int arr[3] = {3, 2, 4};
   int rtrnSize = 2;

   int* out = twoSum(arr, 4, 6, &rtrnSize);
   printf("[%d, %d]\n", out[0], out[1]);
}
