#include <stdio.h>
#include <stdlib.h>

// Comparison function to sort integers in descending order
int compare_desc(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}

// Comparison function to sort integers in ascending order
int compare_asc(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int b, n, m;
    // Read budget, number of keyboards, and number of drives
    if (scanf("%d %d %d", &b, &n, &m) != 3) return 0;

    int* keyboards = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &keyboards[i]) != 1) return 0;
    }

    int* drives = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) {
        if (scanf("%d", &drives[i]) != 1) return 0;
    }

    // Sort keyboards in descending order and drives in ascending order
    qsort(keyboards, n, sizeof(int), compare_desc);
    qsort(drives, m, sizeof(int), compare_asc);

    int max_spent = -1;
    int i = 0; // Pointer for keyboards
    int j = 0; // Pointer for drives

    // Two-pointer search loop
    while (i < n && j < m) {
        int current_sum = keyboards[i] + drives[j];

        if (current_sum <= b) {
            if (current_sum > max_spent) {
                max_spent = current_sum;
            }
            j++; // Try to spend more by choosing a pricier drive
        } else {
            i++; // Exceeded budget, move to a cheaper keyboard
        }
    }

    // Print the final result directly to stdout
    printf("%d\n", max_spent);

    free(keyboards);
    free(drives);
    return 0;
}
