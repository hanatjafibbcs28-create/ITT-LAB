#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

// Structure for hash map to count vertex occurrences
typedef struct {
    long long key;
    int count;
} HashEntry;

// Simple hash map configuration for counting pairs
#define HASH_SIZE 100003
HashEntry hashTable[HASH_SIZE];

void init_hash() {
    for (int i = 0; i < HASH_SIZE; i++) {
        hashTable[i].key = -1;
        hashTable[i].count = 0;
    }
}

void insert_hash(long long key) {
    int idx = (int)((key % HASH_SIZE + HASH_SIZE) % HASH_SIZE);
    while (hashTable[idx].key != -1 && hashTable[idx].key != key) {
        idx = (idx + 1) % HASH_SIZE;
    }
    hashTable[idx].key = key;
    hashTable[idx].count++;
}

bool isRectangleCover(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    if (rectanglesSize == 0) return false;

    // Initialize large bounding box coordinates
    int minX = rectangles[0][0], minY = rectangles[0][1];
    int maxX = rectangles[0][2], maxY = rectangles[0][3];
    long long totalArea = 0;

    init_hash();

    for (int i = 0; i < rectanglesSize; i++) {
        int x1 = rectangles[i][0], y1 = rectangles[i][1];
        int x2 = rectangles[i][2], y2 = rectangles[i][3];

        // Update overall bounding box bounds
        if (x1 < minX) minX = x1;
        if (y1 < minY) minY = y1;
        if (x2 > maxX) maxX = x2;
        if (y2 > maxY) maxY = y2;

        // Add up area of current rectangle
        totalArea += (long long)(x2 - x1) * (y2 - y1);

        // Apply an offset of 100000 to keep all coordinates non-negative before shifting
        long long ux1 = (long long)x1 + 100000;
        long long uy1 = (long long)y1 + 100000;
        long long ux2 = (long long)x2 + 100000;
        long long uy2 = (long long)y2 + 100000;

        // Encode 4 vertices into safe 64-bit keys
        long long v1 = (ux1 << 32) | uy1;
        long long v2 = (ux1 << 32) | uy2;
        long long v3 = (ux2 << 32) | uy1;
        long long v4 = (ux2 << 32) | uy2;

        insert_hash(v1);
        insert_hash(v2);
        insert_hash(v3);
        insert_hash(v4);
    }

    // Check 1: Check if total area matches overall bounding box area
    long long expectedArea = (long long)(maxX - minX) * (maxY - minY);
    if (totalArea != expectedArea) return false;

    // Apply offset to target bounding corners for validation
    long long u_minX = (long long)minX + 100000;
    long long u_minY = (long long)minY + 100000;
    long long u_maxX = (long long)maxX + 100000;
    long long u_maxY = (long long)maxY + 100000;

    // Check 2: Verify the 4 primary bounding corners appear exactly once
    long long corners[4] = {
        (u_minX << 32) | u_minY,
        (u_minX << 32) | u_maxY,
        (u_maxX << 32) | u_minY,
        (u_maxX << 32) | u_maxY
    };

    // Verify all hash items
    int cornerCount = 0;
    for (int i = 0; i < HASH_SIZE; i++) {
        if (hashTable[i].key != -1) {
            long long k = hashTable[i].key;
            int count = hashTable[i].count;

            bool isCorner = (k == corners[0] || k == corners[1] || k == corners[2] || k == corners[3]);
            if (isCorner) {
                if (count != 1) return false; // Outer bounding box corners must occur exactly once
                cornerCount++;
            } else {
                if (count % 2 != 0) return false; // Internal shared corners must appear an even number of times
            }
        }
    }

    return cornerCount == 4;
}
