#include <stdio.h>
#include <stdlib.h>
int main() {
    int n;
    // Read the total number of bird sightings
    if (scanf("%d", &n) != 1) return 0;

    // Fixed frequency array for types 1 to 5 (initialized to 0)
    int freq[6] = {0};
    
    for (int i = 0; i < n; i++) {
        int bird_type;
        if (scanf("%d", &bird_type) == 1) {
            freq[bird_type]++;
        }
    }

    int max_count = 0;
    int result_id = 1;

    // Check types from 1 to 5 in ascending order
    for (int type = 1; type <= 5; type++) {
        // If we find a strictly greater frequency, update our result
        if (freq[type] > max_count) {
            max_count = freq[type];
            result_id = type;
        }
    }

    // Print the final result directly to stdout
    printf("%d\n", result_id);

    return 0;
}
