#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned arrays and *returnColumnSizes array must be separately allocated.
 */
int** intervalIntersection(int** firstList, int firstListSize, int* firstListColSize, 
                            int** secondList, int secondListSize, int* secondListColSize, 
                            int* returnSize, int** returnColumnSizes) {
    
    // Maximum possible number of intersection intervals is the sum of both lists
    int maxIntersections = firstListSize + secondListSize;
    
    // Allocate return buffer
    int** res = (int**)malloc(maxIntersections * sizeof(int*));
    *returnColumnSizes = (int*)malloc(maxIntersections * sizeof(int));
    *returnSize = 0;
    
    int i = 0, j = 0;
    while (i < firstListSize && j < secondListSize) {
        // Determine the potential intersection range
        int start = firstList[i][0] > secondList[j][0] ? firstList[i][0] : secondList[j][0];
        int end = firstList[i][1] < secondList[j][1] ? firstList[i][1] : secondList[j][1];
        
        // If a valid intersection exists, store it
        if (start <= end) {
            res[*returnSize] = (int*)malloc(2 * sizeof(int));
            res[*returnSize][0] = start;
            res[*returnSize][1] = end;
            (*returnColumnSizes)[*returnSize] = 2;
            (*returnSize)++;
        }
        
        // Move the pointer that belongs to the interval ending first
        if (firstList[i][1] < secondList[j][1]) {
            i++;
        } else {
            j++;
        }
    }
    
    // Shrink allocation down to exact result fit size if required
    if (*returnSize == 0) {
        free(res);
        free(*returnColumnSizes);
        return NULL;
    }
    
    return res;
}
