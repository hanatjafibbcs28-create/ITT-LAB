#include <stdlib.h>
#include <string.h>

// Custom comparator function returning 1 if str1 > str2, -1 if str1 < str2, 0 if equal
inline int compare_num_strs(const char* str1, const char* str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    if (len1 > len2) return 1;
    if (len1 < len2) return -1;
    
    int cmp = strcmp(str1, str2);
    if (cmp > 0) return 1;
    if (cmp < 0) return -1;
    return 0;
}

// In-place string pointer swap
inline void swap_strs(char** a, char** b) {
    char* temp = *a;
    *a = *b;
    *b = temp;
}

// Quickselect selection routine to find the k-th largest value in descending order
void quickselect(char** arr, int left, int right, int k) {
    if (left >= right) return;
    
    // Choose the middle element as pivot to prevent bad case regressions
    int mid = left + (right - left) / 2;
    char* pivot = arr[mid];
    
    int i = left - 1;
    int j = right + 1;
    
    while (1) {
        // Sorting in descending order for "largest" element extraction
        do { i++; } while (compare_num_strs(arr[i], pivot) > 0);
        do { j--; } while (compare_num_strs(arr[j], pivot) < 0);
        
        if (i >= j) break;
        swap_strs(&arr[i], &arr[j]);
    }
    
    int left_length = j - left + 1;
    if (k <= left_length) {
        quickselect(arr, left, j, k);
    } else {
        quickselect(arr, j + 1, right, k - left_length);
    }
}

char* kthLargestNumber(char** nums, int numsSize, int k) {
    // Partition the string pointer array so the kth largest sits precisely at index k-1
    quickselect(nums, 0, numsSize - 1, k);
    return nums[k - 1];
}
