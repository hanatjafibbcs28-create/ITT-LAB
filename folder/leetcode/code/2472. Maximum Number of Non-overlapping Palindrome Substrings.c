#include <stdio.h>
#include <string.h>
#include <stdbool.h>
bool isPalindrome(const char* s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}
int maxPalindromes(char* s, int k) {
    int n = strlen(s);
    int ans = 0;
    int last_end = -1; 
    for (int i = 0; i < n; i++) {
        int start1 = i - k + 1;
        if (start1 > last_end && isPalindrome(s, start1, i)) {
            ans++;
            last_end = i;
            continue; 
        }
        int start2 = i - k;
        if (start2 > last_end && isPalindrome(s, start2, i)) {
            ans++;
            last_end = i;
        }
    }
    return ans;
}
