#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    // Read the number of games
    if (scanf("%d", &n) != 1) return 0;

    int* scores = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &scores[i]) != 1) return 0;
    }

    // Initialize highest and lowest with the score of the first game
    int highest = scores[0];
    int lowest = scores[0];
    
    int high_count = 0;
    int low_count = 0;

    // Iterate through the remaining games
    for (int i = 1; i < n; i++) {
        if (scores[i] > highest) {
            highest = scores[i];
            high_count++; // Broke best record
        } else if (scores[i] < lowest) {
            lowest = scores[i];
            low_count++;  // Broke worst record
        }
    }

    // Print the results space-separated as expected
    printf("%d %d\n", high_count, low_count);

    free(scores);
    return 0;
}
