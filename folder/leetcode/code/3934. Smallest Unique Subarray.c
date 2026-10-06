#include <stdlib.h>

typedef unsigned long long ull;

static int works(int *a, int n, int len) {
    int count = n - len + 1;
    int size = 1;

    while (size < count * 2) {
        size <<= 1;
    }

    ull *table = calloc(size, sizeof(ull));
    unsigned char *freq = calloc(size, sizeof(unsigned char));

    const ull base = 1000003ULL;
    ull power = 1;
    ull hash = 0;

    for (int i = 1; i < len; i++) {
        power *= base;
    }

    for (int i = 0; i < len; i++) {
        hash = hash * base + (unsigned int)a[i];
    }

    for (int start = 0; start < count; start++) {
        int pos = (int)(
            (hash * 11995408973635179863ULL) &
            (size - 1)
        );

        while (freq[pos] && table[pos] != hash) {
            pos = (pos + 1) & (size - 1);
        }

        if (!freq[pos]) {
            table[pos] = hash;
            freq[pos] = 1;
        } else if (freq[pos] < 2) {
            freq[pos]++;
        }

        if (start + len < n) {
            hash =
                (hash - (ull)(unsigned int)a[start] * power)
                * base
                + (unsigned int)a[start + len];
        }
    }

    for (int i = 0; i < size; i++) {
        if (freq[i] == 1) {
            free(table);
            free(freq);
            return 1;
        }
    }

    free(table);
    free(freq);

    return 0;
}

int smallestUniqueSubarray(int *nums, int numsSize) {
    int left = 1;
    int right = numsSize;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (works(nums, numsSize, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
