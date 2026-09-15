#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k;
    // Read the total number of items and the index Anna didn't eat
    if (scanf("%d %d", &n, &k) != 2) return 0;

    int* bill = (int*)malloc(n * sizeof(int));
    long long total_shared_sum = 0;

    for (int i = 0; i < n; i++) {
        if (scanf("%d", &bill[i]) != 1) return 0;
        // Sum all items EXCEPT the one Anna didn't eat
        if (i != k) {
            total_shared_sum += bill[i];
        }
    }

    int b;
    // Read the amount Brian charged Anna
    if (scanf("%d", &b) != 1) return 0;

    int fair_share = total_shared_sum / 2;

    if (b == fair_share) {
        printf("Bon Appetit\n");
    } else {
        printf("%d\n", b - fair_share);
    }

    free(bill);
    return 0;
}
