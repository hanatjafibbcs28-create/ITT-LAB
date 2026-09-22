#include <stdlib.h>

// Inline function to get squared distance
inline long long get_dist(int* p) {
    return (long long)p[0] * p[0] + (long long)p[1] * p[1];
}

// In-place pointer swap using simple address tracking
inline void swap_points(int** points, int i, int j) {
    int* temp = points[i];
    points[i] = points[j];
    points[j] = temp;
}

// Quickselect selection routine
void quickselect(int** points, int left, int right, int k) {
    if (left >= right) return;
    
    // Choose a middle element as pivot to prevent worst-case scenarios
    int mid = left + (right - left) / 2;
    long long pivot_dist = get_dist(points[mid]);
    
    int i = left - 1;
    int j = right + 1;
    
    while (1) {
        do { i++; } while (get_dist(points[i]) < pivot_dist);
        do { j--; } while (get_dist(points[j]) > pivot_dist);
        
        if (i >= j) break;
        swap_points(points, i, j);
    }
    
    // j marks the end of the left partition
    int left_length = j - left + 1;
    if (k <= left_length) {
        quickselect(points, left, j, k);
    } else {
        quickselect(points, j + 1, right, k - left_length);
    }
}

int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int** returnColumnSizes) {
    // Partition the array so the k closest points occupy indices 0 to k-1
    quickselect(points, 0, pointsSize - 1, k);
    
    // Allocate final structures
    int** result = (int**)malloc(k * sizeof(int*));
    *returnColumnSizes = (int*)malloc(k * sizeof(int));
    *returnSize = k;
    
    // Direct assignment instead of re-allocation yields ultra-fast performance
    for (int i = 0; i < k; i++) {
        result[i] = points[i];
        (*returnColumnSizes)[i] = 2;
    }
    
    return result;
}
