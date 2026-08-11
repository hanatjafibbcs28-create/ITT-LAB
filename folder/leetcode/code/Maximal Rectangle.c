#include <stdlib.h>
typedef struct {
    int height;
    int start;
} Pair;
static int max_int(int a, int b) { return a > b ? a : b; }
static int calculate(int* h, int n, Pair* st) {
    int top = 0;
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        int start = i;
        while (top > 0 && st[top - 1].height > h[i]) {
            Pair p = st[--top];
            maxArea = max_int(maxArea, p.height * (i - p.start));
            start = p.start;
        }
        st[top++] = (Pair){h[i], start};
    }
    while (top > 0) {
        Pair p = st[--top];
        maxArea = max_int(maxArea, p.height * (n - p.start));
    }
    return maxArea;
}
int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {
    int row = matrixSize;
    if (row == 0) return 0;
    int col = matrixColSize[0];
    if (col == 0) return 0;
    int* heights = (int*)calloc((size_t)col, sizeof(int));
    Pair* st = (Pair*)malloc(sizeof(Pair) * col);
    int ans = 0;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (matrix[i][j] == '1') heights[j] += 1;
            else heights[j] = 0;
        }
        int area = calculate(heights, col, st);
        if (area > ans) ans = area;
    }
    free(st);
    free(heights);
    return ans;
}
