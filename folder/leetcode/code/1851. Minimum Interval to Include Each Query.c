#include <stdlib.h>
#include <string.h>
typedef struct {
    int val;
    int idx;
} QueryNode;
typedef struct {
    int size;
    int right;
} HeapNode;
int compare_intervals(const void* a, const void* b) {
    int* ia = *(int**)a;
    int* ib = *(int**)b;
    return ia[0] - ib[0];
}
int compare_queries(const void* a, const void* b) {
    return ((QueryNode*)a)->val - ((QueryNode*)b)->val;
}
void push_heap(HeapNode* heap, int* heapSize, int size, int right) {
    int i = (*heapSize)++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p].size <= size) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i].size = size;
    heap[i].right = right;
}

void pop_heap(HeapNode* heap, int* heapSize) {
    (*heapSize)--;
    if (*heapSize <= 0) return;
    HeapNode last = heap[*heapSize];
    int i = 0;
    while (2 * i + 1 < *heapSize) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int child = left;
        if (right < *heapSize && heap[right].size < heap[left].size) {
            child = right;
        }
        if (last.size <= heap[child].size) break;
        heap[i] = heap[child];
        i = child;
    }
    heap[i] = last;
}
int* minInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* queries, int queriesSize, int* returnSize) {
    qsort(intervals, intervalsSize, sizeof(int*), compare_intervals);
    QueryNode* qNodes = (QueryNode*)malloc(queriesSize * sizeof(QueryNode));
    for (int i = 0; i < queriesSize; i++) {
        qNodes[i].val = queries[i];
        qNodes[i].idx = i;
    }
    qsort(qNodes, queriesSize, sizeof(QueryNode), compare_queries);
    HeapNode* heap = (HeapNode*)malloc(intervalsSize * sizeof(HeapNode));
    int heapSize = 0;
    int* res = (int*)malloc(queriesSize * sizeof(int));
    *returnSize = queriesSize;
    int intervalIdx = 0;
    for (int i = 0; i < queriesSize; i++) {
        int qVal = qNodes[i].val;
        int qIdx = qNodes[i].idx;
        while (intervalIdx < intervalsSize && intervals[intervalIdx][0] <= qVal) {
            int l = intervals[intervalIdx][0];
            int r = intervals[intervalIdx][1];
            push_heap(heap, &heapSize, r - l + 1, r);
            intervalIdx++;
        }
        while (heapSize > 0 && heap[0].right < qVal) {
            pop_heap(heap, &heapSize);
        }
        if (heapSize > 0) {
            res[qIdx] = heap[0].size;
        } else {
            res[qIdx] = -1;
        }
    }
    free(qNodes);
    free(heap);
    return res;
}
