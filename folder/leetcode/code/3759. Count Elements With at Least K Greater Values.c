#include <stdlib.h>

// Quickselect to find the element at the target index in O(N) average time
int quickselect(int* nums, int left, int right, int target_idx) {
    if (left == right) return nums[left];
    
    // Choose a middle pivot to avoid worst-case regressions
    int mid = left + (right - left) / 2;
    int pivot = nums[mid];
    
    int i = left - 1;
    int j = right + 1;
    
    while (1) {
        do { i++; } while (nums[i] < pivot);
        do { j--; } while (nums[j] > pivot);
        
        if (i >= j) break;
        
        // In-place swap inline to prevent structural macro or linking issues
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    if (target_idx <= j) {
        return quickselect(nums, left, j, target_idx);
    } else {
        return quickselect(nums, j + 1, right, target_idx);
    }
}

int countElements(int* nums, int numsSize, int k) {
    // Edge case: If k is 0, all elements have at least 0 elements greater than them
    if (k == 0) return numsSize;
    
    // Find the boundary value at sorted index (numsSize - k)
    int target_val = quickselect(nums, 0, numsSize - 1, numsSize - k);
    
    // Count how many elements are strictly smaller than our target boundary value
    int qualifiedCount = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < target_val) {
            qualifiedCount++;
        }
    }
    
    return qualifiedCount;
}
