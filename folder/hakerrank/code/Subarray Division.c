#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    // Read the number of chocolate squares
    if (scanf("%d", &n) != 1) return 0;

    int* s = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &s[i]) != 1) return 0;
    }

    int d, m;
    // Read Ron's birth day and birth month
    if (scanf("%d %d", &d, &m) != 2) return 0;

    int count = 0;

    // We can only look for segments if the chocolate bar is long enough
    if (n >= m) {
        int current_sum = 0;

        // Calculate the sum of the first window of size m
        for (int i = 0; i < m; i++) {
            current_sum += s[i];
        }

        // Check if the first window matches the target day
        if (current_sum == d) {
            count++;
        }

        // Slide the window across the rest of the array
        for (int i = m; i < n; i++) {
            // Add the new element entering the window, subtract the one leaving
            current_sum += s[i] - s[i - m];
            
            if (current_sum == d) {
                count++;
            }
        }
    }

    // Print the result directly to stdout
    printf("%d\n", count);

    free(s);
    return 0;
}
