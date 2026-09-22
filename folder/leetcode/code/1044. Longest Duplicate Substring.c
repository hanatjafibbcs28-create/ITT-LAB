#include <stdlib.h>
#include <string.h>

#define MAX_STATES 60005

typedef struct {
    int len;
    int link;
    int next[26];
    int cnt;
    int first_end; // Tracks the first absolute ending index of this state's pattern
} State;

State st[MAX_STATES];
int sz, last;

void sam_init() {
    sz = 1;
    last = 0;
    st[0].len = 0;
    st[0].link = -1;
    st[0].cnt = 0;
    st[0].first_end = -1;
    memset(st[0].next, -1, sizeof(st[0].next));
}

void sam_extend(char c, int idx) {
    int cur = sz++;
    st[cur].len = st[last].len + 1;
    st[cur].cnt = 1;
    st[cur].first_end = idx; // Store exact string character coordinate position
    memset(st[cur].next, -1, sizeof(st[cur].next));
    
    int p = last;
    while (p != -1 && st[p].next[c - 'a'] == -1) {
        st[p].next[c - 'a'] = cur;
        p = st[p].link;
    }
    
    if (p == -1) {
        st[cur].link = 0;
    } else {
        int q = st[p].next[c - 'a'];
        if (st[p].len + 1 == st[q].len) {
            st[cur].link = q;
        } else {
            int clone = sz++;
            st[clone].len = st[p].len + 1;
            st[clone].link = st[q].link;
            st[clone].cnt = 0;
            st[clone].first_end = st[q].first_end; // Clone copies structural positional reference
            memcpy(st[clone].next, st[q].next, sizeof(st[q].next));
            
            while (p != -1 && st[p].next[c - 'a'] == q) {
                st[p].next[c - 'a'] = clone;
                p = st[p].link;
            }
            st[q].link = st[cur].link = clone;
        }
    }
    last = cur;
}

char* longestDupSubstring(char* s) {
    int n = strlen(s);
    if (n == 0) return "";
    
    sam_init();
    for (int i = 0; i < n; i++) {
        sam_extend(s[i], i);
    }
    
    // Bucket sort / Topo-sort setup
    int* bucket_count = (int*)calloc(n + 1, sizeof(int));
    int* order = (int*)malloc(sz * sizeof(int));
    
    for (int i = 0; i < sz; i++) bucket_count[st[i].len]++;
    for (int i = 1; i <= n; i++) bucket_count[i] += bucket_count[i - 1];
    for (int i = 0; i < sz; i++) order[--bucket_count[st[i].len]] = i;
    
    // Accumulate substring frequency configurations up the links tree
    for (int i = sz - 1; i >= 1; i--) {
        int u = order[i];
        if (st[u].link != -1) {
            st[st[u].link].cnt += st[u].cnt;
        }
    }
    
    int max_len = 0;
    int best_end = 0;
    
    // Identify the longest state that occurred at least 2 times
    for (int i = 1; i < sz; i++) {
        if (st[i].cnt >= 2 && st[i].len > max_len) {
            max_len = st[i].len;
            best_end = st[i].first_end;
        }
    }
    
    // Safe substring replication construction 
    char* result = (char*)malloc((max_len + 1) * sizeof(char));
    if (max_len > 0) {
        strncpy(result, s + (best_end - max_len + 1), max_len);
    }
    result[max_len] = '\0';
    
    free(bucket_count);
    free(order);
    
    return result;
}
