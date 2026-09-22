#include <string.h>

void wiggleSort(int* nums, int numsSize) {
    int bucket[5001] = {0};
    
    // Step 1: Count frequencies of each number
    for (int i = 0; i < numsSize; i++) {
        bucket[nums[i]]++;
    }
    
    int j = 5000;
    
    // Step 2: Fill odd indices (1, 3, 5, ...) from largest to smallest
    for (int i = 1; i < numsSize; i += 2) {
        while (bucket[j] == 0) j--;
        nums[i] = j;
        bucket[j]--;
    }
    
    // Step 3: Fill even indices (0, 2, 4, ...) with the remaining elements
    for (int i = 0; i < numsSize; i += 2) {
        while (bucket[j] == 0) j--;
        nums[i] = j;
        bucket[j]--;
    }
}
