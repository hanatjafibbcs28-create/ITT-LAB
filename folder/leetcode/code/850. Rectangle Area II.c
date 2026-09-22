#include <stdlib.h>
#include <string.h>

#define MOD 1000000007

typedef struct {
    int x;
    int y1, y2;
    int type; // +1 for left edge (insertion), -1 for right edge (removal)
} Event;

// Comparator for X-axis event points
int compare_events(const void* a, const void* b) {
    Event* e1 = (Event*)a;
    Event* e2 = (Event*)b;
    if (e1->x != e2->x) return (e1->x < e2->x) ? -1 : 1;
    return (e1->type < e2->type) ? -1 : 1;
}

// Comparator for Y-coordinate compression
int compare_ints(const void* a, const void* b) {
    int va = *(const int*)a;
    int vb = *(const int*)b;
    return (va < vb) ? -1 : (va > vb) ? 1 : 0;
}

// Global segment tree structures to avoid constant reallocation overhead
int tree_cnt[2005];
long long tree_len[2005];
int* y_space;

// Update the segment tree dynamically based on intervals
void update_tree(int node, int start, int end, int l, int r, int val) {
    if (l <= start && end <= r) {
        tree_cnt[node] += val;
    } else {
        int mid = (start + end) / 2;
        if (l <= mid) update_tree(2 * node, start, mid, l, r, val);
        if (r > mid) update_tree(2 * node + 1, mid + 1, end, l, r, val);
    }

    if (tree_cnt[node] > 0) {
        tree_len[node] = y_space[end + 1] - y_space[start];
    } else if (start == end) {
        tree_len[node] = 0;
    } else {
        tree_len[node] = tree_len[2 * node] + tree_len[2 * node + 1];
    }
}

// Binary search helper to query compressed Y-space array indexes quickly
int get_compressed_idx(int value, int size) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (y_space[mid] == value) return mid;
        if (y_space[mid] < value) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int rectangleArea(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    if (rectanglesSize == 0) return 0;

    int num_events = 2 * rectanglesSize;
    Event* events = (Event*)malloc(num_events * sizeof(Event));
    int* unique_y = (int*)malloc(num_events * sizeof(int));
    
    int idx = 0;
    for (int i = 0; i < rectanglesSize; i++) {
        int x1 = rectangles[i][0], y1 = rectangles[i][1];
        int x2 = rectangles[i][2], y2 = rectangles[i][3];
        
        events[idx] = (Event){x1, y1, y2, 1};
        unique_y[idx++] = y1;
        
        events[idx] = (Event){x2, y1, y2, -1};
        unique_y[idx++] = y2;
    }

    qsort(events, num_events, sizeof(Event), compare_events);
    qsort(unique_y, num_events, sizeof(int), compare_ints);

    // Coordinate Compression on Y axis values
    int y_size = 0;
    for (int i = 0; i < num_events; i++) {
        if (y_size == 0 || unique_y[i] != unique_y[y_size - 1]) {
            unique_y[y_size++] = unique_y[i];
        }
    }
    y_space = unique_y;

    // Reset segment tree memory layers
    memset(tree_cnt, 0, sizeof(tree_cnt));
    memset(tree_len, 0, sizeof(tree_len));

    long long total_area = 0;
    
    for (int i = 0; i < num_events - 1; i++) {
        int y1_idx = get_compressed_idx(events[i].y1, y_size);
        int y2_idx = get_compressed_idx(events[i].y2, y_size);
        
        // Update interval range [y1_idx, y2_idx - 1] in tree leaf boundaries
        update_tree(1, 0, y_size - 2, y1_idx, y2_idx - 1, events[i].type);
        
        long long width = events[i + 1].x - events[i].x;
        if (width > 0) {
            total_area = (total_area + (width * tree_len[1])) % MOD;
        }
    }

    free(events);
    free(unique_y);

    return (int)total_area;
}
