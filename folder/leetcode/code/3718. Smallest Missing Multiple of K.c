int missingMultiple(int* nums, int numsSize, int k) {
    int present[101] = {0}; 
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] <= 100) {
            present[nums[i]] = 1;
        }
    }
    int multiple = k;
    while (multiple <= 100 && present[multiple]) {
        multiple += k;
    }   
    return multiple;
}
