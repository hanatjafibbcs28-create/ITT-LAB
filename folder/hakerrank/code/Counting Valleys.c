#include <stdio.h>
#include <stdlib.h>

int main() {
    int steps;
    // Read the number of steps
    if (scanf("%d", &steps) != 1) return 0;

    // Allocate memory for the path string (+1 for the null terminator)
    char* path = (char*)malloc((steps + 1) * sizeof(char));
    if (scanf("%s", path) != 1) {
        free(path);
        return 0;
    }

    int altitude = 0;
    int valley_count = 0;

    for (int i = 0; i < steps; i++) {
        if (path[i] == 'U') {
            altitude++;
            // If we just reached sea level from below, a valley has ended
            if (altitude == 0) {
                valley_count++;
            }
        } else if (path[i] == 'D') {
            altitude--;
        }
    }

    // Print the final result directly to stdout
    printf("%d\n", valley_count);

    free(path);
    return 0;
}
