#include <stdlib.h>
long long sumScores(char *s) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }
    int *z = calloc(n, sizeof(int));
    int left = 0;
    int right = 0;
    long long answer = n;
    for (int i = 1; i < n; i++) {
        if (i <= right) {
            int remaining = right - i + 1;

            if (z[i - left] < remaining) {
                z[i] = z[i - left];
            } else {
                z[i] = remaining;
            }
        }
        while (i + z[i] < n &&
               s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        if (i + z[i] - 1 > right) {
            left = i;
            right = i + z[i] - 1;
        }
        answer += z[i];
    }
    free(z);
    return answer;
}
