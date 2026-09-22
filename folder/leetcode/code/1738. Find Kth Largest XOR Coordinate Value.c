#include <stdlib.h>

// In-place value swap
inline void swap_vals(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Quickselect selection routine to find the k-th largest value
void quickselect(int* arr, int left, int right, int k) {
    if (left >= right) return;
    
    // Choose the middle element as pivot
    int mid = left + (right - left) / 2;
    int pivot = arr[mid];
    
    int i = left - 1;
    int j = right + 1;
    
    while (1) {
        do { i++; } while (arr[i] > pivot); // Sorting in descending order for "largest"
        do { j--; } while (arr[j] < pivot);
        
        if (i >= j) break;
        swap_vals(&arr[i], &arr[j]);
    }
    
    int left_length = j - left + 1;
    if (k <= left_length) {
        quickselect(arr, left, j, k);
    } else {
        quickselect(arr, j + 1, right, k - left_length);
    }
}

int kthLargestValue(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int m = matrixSize;
    int n = matrixColSize[0];
    int total_elements = m * n;
    
    // Flattened array to store all calculated prefix XOR values
    int* xor_values = (int*)malloc(total_elements * sizeof(int));
    int idx = 0;
    
    // Dynamic 2D array allocated tracking matrix for prefix calculations
    int** xor_matrix = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        xor_matrix[i] = (int*)malloc(n * sizeof(int));
    }
    
    // Compute the 2D Prefix XOR values
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int current_xor = matrix[i][j];
            if (i > 0) current_xor ^= xor_matrix[i-1][j];
            if (j > 0) current_xor ^= xor_matrix[i][j-1];
            if (i > 0 && j > 0) current_xor ^= xor_matrix[i-1][j-1];
            
            xor_matrix[i][j] = current_xor;
            xor_values[idx++] = current_xor;
        }
    }
    
    // Find the k-th largest element using Quickselect (1-indexed input matching)
    quickselect(xor_values, 0, total_elements - 1, k);
    
    int result = xor_values[k - 1];
    
    // Free allocated memory
    for (int i = 0; i < m; i++) {
        free(xor_matrix[i]);
    }
    free(xor_matrix);
    free(xor_values);
    
    return result;
}
