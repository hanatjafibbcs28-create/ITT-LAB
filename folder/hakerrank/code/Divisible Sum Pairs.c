#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k;
    // Read the array size and the divisor k
    if (scanf("%d %d", &n, &k) != 2) return 0;

    int* ar = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &ar[i]) != 1) return 0;
    }

    // Calloc initializes the tracking array to 0
    // The maximum possible remainder is k-1
    int* remainder_counts = (int*)calloc(k, sizeof(int));
    int pair_count = 0;

    for (int i = 0; i < n; i++) {
        int rem = ar[i] % k;
        
        // Find the matching remainder needed to sum to a multiple of k
        int complement = (k - rem) % k;
        
        // Add the number of times we've seen this complement so far
        pair_count += remainder_counts[complement];
        
        // Record the current remainder in our frequency tracker
        remainder_counts[rem]++;
    }

    // Print the final result directly to stdout
    printf("%d\n", pair_count);

    free(ar);
    free(remainder_counts);
    return 0;
}
