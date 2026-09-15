#include <stdio.h>
#include <stdlib.h>

// Function to find the Greatest Common Divisor
int gcd(int x, int y) {
    while (y != 0) {
        int temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}

// Function to find the Least Common Multiple
int lcm(int x, int y) {
    if (x == 0 || y == 0) return 0;
    return (x * y) / gcd(x, y);
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;

    int* a = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &a[i]) != 1) return 0;
    }

    int* b = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) {
        if (scanf("%d", &b[i]) != 1) return 0;
    }

    // Find LCM of all elements in array 'a'
    int lcm_a = a[0];
    for (int i = 1; i < n; i++) {
        lcm_a = lcm(lcm_a, a[i]);
    }

    // Find GCD of all elements in array 'b'
    int gcd_b = b[0];
    for (int i = 1; i < m; i++) {
        gcd_b = gcd(gcd_b, b[i]);
    }

    int count = 0;
    int multiple = lcm_a;

    // Count multiples of lcm_a that evenly divide gcd_b
    while (multiple <= gcd_b) {
        if (gcd_b % multiple == 0) {
            count++;
        }
        multiple += lcm_a;
    }

    // Print the final result to stdout
    printf("%d\n", count);

    free(a);
    free(b);
    return 0;
}
