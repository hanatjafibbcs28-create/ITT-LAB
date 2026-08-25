#include <stdlib.h>
#include <string.h>
#define MAX_VAL 20005
#define OFFSET 10002
void update(int* bit, int index, int val) {
    while (index < MAX_VAL) {
        bit[index] += val;
        index += index & (-index);
    }
}
int query(int* bit, int index) {
    int sum = 0;
    while (index > 0) {
        sum += bit[index];
        index -= index & (-index);
    }
    return sum;
}
int* countSmaller(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    if (numsSize == 0) return NULL;
    int* counts = (int*)malloc(numsSize * sizeof(int));
    int bit[MAX_VAL] = {0};
    for (int i = numsSize - 1; i >= 0; i--) {
        int shifted_val = nums[i] + OFFSET;
        counts[i] = query(bit, shifted_val - 1);
        update(bit, shifted_val, 1);
    }
    return counts;
}
