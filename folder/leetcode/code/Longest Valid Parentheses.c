#include <string.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))
int longestValidParentheses(char* s) {
    int len = strlen(s);
    if (len == 0) return 0;
    int left = 0, right = 0;
    int max_len = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            left++;
        } else {
            right++;
        }
        if (left == right) {
            max_len = MAX(max_len, 2 * right);
        } else if (right > left) {
            left = 0;
            right = 0;
        }
    }
    left = 0;
    right = 0;
    for (int i = len - 1; i >= 0; i--) {
        if (s[i] == '(') {
            left++;
        } else {
            right++;
        }
        if (left == right) {
            max_len = MAX(max_len, 2 * left);
        } else if (left > right) {
            left = 0;
            right = 0;
        }
    }
    return max_len;
}
