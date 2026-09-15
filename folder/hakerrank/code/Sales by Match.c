#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    // Read the total number of socks
    if (scanf("%d", &n) != 1) return 0;

    // Fixed color tracking array for constraints up to 100 (initialized to 0)
    int color_counts[101] = {0};
    
    for (int i = 0; i < n; i++) {
        int color;
        if (scanf("%d", &color) == 1) {
            color_counts[color]++;
        }
    }

    int total_pairs = 0;

    // Calculate pairs for each possible color index
    for (int i = 1; i <= 100; i++) {
        total_pairs += color_counts[i] / 2;
    }

    // Print the final result directly to stdout
    printf("%d\n", total_pairs);

    return 0;
}
