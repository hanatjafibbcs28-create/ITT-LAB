int missingInteger(int* nums, int numsSize) {
    int sum = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1] + 1) {
            sum += nums[i];
        } else {
            break; 
        }
    }
    int present[52] = {0};
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] <= 51) {
            present[nums[i]] = 1;
        }
    }
    while (sum <= 50 && present[sum]) {
        sum++;
    }
    return sum;
}
