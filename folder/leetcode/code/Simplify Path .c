#include <string.h>
char* simplifyPath(char* path) {
    int len = strlen(path);
    int write = 0; 
    int segment_starts[len / 2 + 1];
    int top = -1;
    for (int read = 0; read < len; ) {
        while (read < len && path[read] == '/') {
            read++;
        }
        if (read >= len) break;
        int start = read;
        while (read < len && path[read] != '/') {
            read++;
        }
        int token_len = read - start;
        if (token_len == 1 && path[start] == '.') {
            continue;
        } 
        else if (token_len == 2 && path[start] == '.' && path[start + 1] == '.') {
            if (top >= 0) {
                write = segment_starts[top--];
            }
        } 
        else {
            segment_starts[++top] = write; 
            path[write++] = '/';
            for (int i = 0; i < token_len; i++) {
                path[write++] = path[start + i];
            }
        }
    }
    if (write == 0) {
        path[write++] = '/';
    }
    path[write] = '\0';
    return path;
}
