#include <stdio.h>

int main() {
    int n, p;
    // Read total pages n and the target page p
    if (scanf("%d %d", &n, &p) != 2) return 0;

    // Number of turns from the front
    int from_front = p / 2;

    // Number of turns from the back
    int from_back = (n / 2) - (p / 2);

    // Find the minimum of both paths
    int min_turns = (from_front < from_back) ? from_front : from_back;

    // Print the final result directly to stdout
    printf("%d\n", min_turns);

    return 0;
}
