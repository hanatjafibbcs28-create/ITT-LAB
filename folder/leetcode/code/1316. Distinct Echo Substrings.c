#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define BASE 26
#define MOD1 1000000007
#define MOD2 1000000009

typedef struct {
    long long h1;
    long long h2;
    int len; // Storing length alongside hashes avoids repetition collisions
} SubstringKey;

#define HASH_SIZE 400009
SubstringKey hashTable[HASH_SIZE];
bool hashFilled[HASH_SIZE];

void init_hash_table() {
    memset(hashFilled, 0, sizeof(hashFilled));
}

// Check uniqueness by tracking both the hash of part 'a' and its structural length
bool insert_unique(long long h1, long long h2, int len) {
    unsigned int idx = (unsigned int)(((h1 ^ h2 ^ len) % HASH_SIZE + HASH_SIZE) % HASH_SIZE);
    while (hashFilled[idx]) {
        if (hashTable[idx].h1 == h1 && hashTable[idx].h2 == h2 && hashTable[idx].len == len) {
            return false; 
        }
        idx = (idx + 1) % HASH_SIZE;
    }
    hashTable[idx].h1 = h1;
    hashTable[idx].h2 = h2;
    hashTable[idx].len = len;
    hashFilled[idx] = true;
    return true;
}

int distinctEchoSubstrings(char* text) {
    int n = strlen(text);
    init_hash_table();
    
    long long* pref1 = (long long*)malloc((n + 1) * sizeof(long long));
    long long* pref2 = (long long*)malloc((n + 1) * sizeof(long long));
    long long* pow1 = (long long*)malloc((n + 1) * sizeof(long long));
    long long* pow2 = (long long*)malloc((n + 1) * sizeof(long long));
    
    pref1[0] = 0; pref2[0] = 0;
    pow1[0] = 1;  pow2[0] = 1;
    
    for (int i = 0; i < n; i++) {
        pref1[i + 1] = (pref1[i] * BASE + (text[i] - 'a')) % MOD1;
        pref2[i + 1] = (pref2[i] * BASE + (text[i] - 'a')) % MOD2;
        pow1[i + 1] = (pow1[i] * BASE) % MOD1;
        pow2[i + 1] = (pow2[i] * BASE) % MOD2;
    }
    
    int unique_count = 0;
    
    for (int len = 1; len <= n / 2; len++) {
        for (int i = 0; i <= n - 2 * len; i++) {
            // Hash for the first half 'a'
            long long h1_first = (pref1[i + len] - (pref1[i] * pow1[len]) % MOD1 + MOD1) % MOD1;
            long long h2_first = (pref2[i + len] - (pref2[i] * pow2[len]) % MOD2 + MOD2) % MOD2;
            
            // Hash for the second half 'a'
            long long h1_second = (pref1[i + 2 * len] - (pref1[i + len] * pow1[len]) % MOD1 + MOD1) % MOD1;
            long long h2_second = (pref2[i + 2 * len] - (pref2[i + len] * pow2[len]) % MOD2 + MOD2) % MOD2;
            
            // If both pieces are identical, we check if this specific string 'a' of length 'len' is unique
            if (h1_first == h1_second && h2_first == h2_second) {
                if (insert_unique(h1_first, h2_first, len)) {
                    unique_count++;
                }
            }
        }
    }
    
    free(pref1); free(pref2);
    free(pow1);  free(pow2);
    
    return unique_count;
}
