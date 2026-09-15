import java.util.HashSet;
import java.util.Set;

public class Solution {
    public boolean splitArraySameAverage(int[] nums) {
        int n = nums.length;
        if (n == 1) return false;

        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // Transform array: target subset sum now equals exactly 0
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] * n - totalSum;
        }

        int leftHalfSize = n / 2;
        int rightHalfSize = n - leftHalfSize;

        // Store all possible non-empty subset sums from the left half
        Set<Integer> leftSubsetSums = new HashSet<>();
        
        // Bitmask for left half (1 to 2^leftHalfSize - 1)
        int totalLeftCombinations = 1 << leftHalfSize;
        for (int i = 1; i < totalLeftCombinations; i++) {
            int currentSum = 0;
            for (int j = 0; j < leftHalfSize; j++) {
                if (((i >> j) & 1) == 1) {
                    currentSum += nums[j];
                }
            }
            if (currentSum == 0) return true; // Direct 0 sum found in the left half
            leftSubsetSums.add(currentSum);
        }

        // Generate subset sums for the right half and match with left half
        int totalRightCombinations = 1 << rightHalfSize;
        for (int i = 1; i < totalRightCombinations; i++) {
            int currentSum = 0;
            for (int j = 0; j < rightHalfSize; j++) {
                if (((i >> j) & 1) == 1) {
                    currentSum += nums[leftHalfSize + j];
                }
            }
            if (currentSum == 0) return true; // Direct 0 sum found in the right half

            // If the full right half is taken, we cannot take the full left half 
            // because subset A must leave subset B non-empty.
            if (i == totalRightCombinations - 1) {
                continue;
            }

            // If left half has a value that cancels out the right half sum, we found a match!
            if (leftSubsetSums.contains(-currentSum)) {
                return true;
            }
        }

        return false;
    }
}
