#include <stdlib.h>
#include <string.h>
#define MAXN 50005
typedef struct {
    double y;
    double x1;
    double x2;
    int type;
} Event;
int compare_events(const void* a, const void* b) {
    double yA = ((Event*)a)->y;
    double yB = ((Event*)b)->y;
    if (yA < yB) return -1;
    if (yA > yB) return 1;
    return 0;
}
int compare_doubles(const void* a, const void* b) {
    double va = *(const double*)a;
    double vb = *(const double*)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}
int* cover;
double* tree_len;
double* xs;
void update_tree(int node, int l, int r, int ql, int qr, int val) {
    if (qr <= l || r <= ql) return;
    if (ql <= l && r <= qr) {
        cover[node] += val;
    } else {
        int m = (l + r) / 2;
        update_tree(node * 2, l, m, ql, qr, val);
        update_tree(node * 2 + 1, m, r, ql, qr, val);
    }
    if (cover[node] > 0) {
        tree_len[node] = xs[r] - xs[l];
    } else if (r - l == 1) {
        tree_len[node] = 0;
    } else {
        tree_len[node] = tree_len[node * 2] + tree_len[node * 2 + 1];
    }
}
int find_index(double value, int size) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (xs[mid] == value) return mid;
        if (xs[mid] < value) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    int num_coords = 2 * squaresSize;
    double* all_xs = (double*)malloc(num_coords * sizeof(double));
    Event* events = (Event*)malloc(2 * squaresSize * sizeof(Event));
    int coord_idx = 0;
    int event_idx = 0;
    for (int i = 0; i < squaresSize; i++) {
        double x = squares[i][0];
        double y = squares[i][1];
        double l = squares[i][2];
        all_xs[coord_idx++] = x;
        all_xs[coord_idx++] = x + l;
        events[event_idx++] = (Event){y, x, x + l, 1};
        events[event_idx++] = (Event){y + l, x, x + l, -1};
    }
    qsort(all_xs, num_coords, sizeof(double), compare_doubles);
    xs = (double*)malloc(num_coords * sizeof(double));
    int unique_x_count = 0;
    for (int i = 0; i < num_coords; i++) {
        if (unique_x_count == 0 || all_xs[i] != xs[unique_x_count - 1]) {
            xs[unique_x_count++] = all_xs[i];
        }
    }
    free(all_xs);
    qsort(events, event_idx, sizeof(Event), compare_events);
    cover = (int*)calloc(4 * unique_x_count, sizeof(int));
    tree_len = (double*)calloc(4 * unique_x_count, sizeof(double));
    double total_area = 0;
    double prev_y = events[0].y;
    for (int i = 0; i < event_idx; i++) {
        double curr_y = events[i].y;
        total_area += (curr_y - prev_y) * tree_len[1];
        int ql = find_index(events[i].x1, unique_x_count);
        int qr = find_index(events[i].x2, unique_x_count);
        update_tree(1, 0, unique_x_count - 1, ql, qr, events[i].type);
        prev_y = curr_y;
    }
    memset(cover, 0, 4 * unique_x_count * sizeof(int));
    memset(tree_len, 0, 4 * unique_x_count * sizeof(double));
    double target_half_area = total_area / 2.0;
    double current_accumulated_area = 0;
    prev_y = events[0].y;
    double answer_y = prev_y;
    for (int i = 0; i < event_idx; i++) {
        double curr_y = events[i].y;
        double current_strip_area = (curr_y - prev_y) * tree_len[1];
        if (current_accumulated_area + current_strip_area >= target_half_area) {
            answer_y = prev_y + (target_half_area - current_accumulated_area) / tree_len[1];
            break;
        }
        current_accumulated_area += current_strip_area;
        int ql = find_index(events[i].x1, unique_x_count);
        int qr = find_index(events[i].x2, unique_x_count);
        update_tree(1, 0, unique_x_count - 1, ql, qr, events[i].type);
        prev_y = curr_y;
    }
    free(events);
    free(xs);
    free(cover);
    free(tree_len);
    return answer_y;
}
