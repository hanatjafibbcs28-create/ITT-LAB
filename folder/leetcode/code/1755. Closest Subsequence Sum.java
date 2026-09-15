import java.util.Arrays;

public class Solution {
    public int minAbsDifference(int[] nums, int goal) {
        int n = nums.length;
        int mid = n / 2;
        
        // Generate all subset sums for the left half
        int[] leftSums = generateSubsetSums(nums, 0, mid);
        // Generate all subset sums for the right half
        int[] rightSums = generateSubsetSums(nums, mid, n);
        
        // Sort left subset sums for efficient binary searching
        Arrays.sort(leftSums);
        
        int minDiff = Integer.MAX_VALUE;
        
        // For each sum in the right half, find the closest matching sum in the left half
        for (int rightSum : rightSums) {
            int target = goal - rightSum;
            
            // Binary search for the target in leftSums
            int index = Arrays.binarySearch(leftSums, target);
            
            // If exact value is found, difference is 0
            if (index >= 0) {
                return 0;
            }
            
            // If not found, binarySearch returns (-(insertion point) - 1)
            int insertionPoint = -index - 1;
            
            // Check the element at the insertion point (closest value greater than target)
            if (insertionPoint < leftSums.length) {
                // Cast the long absolute difference back to int safely
                minDiff = Math.min(minDiff, (int) Math.abs((long) leftSums[insertionPoint] + rightSum - goal));
            }
            
            // Check the element just before the insertion point (closest value smaller than target)
            if (insertionPoint > 0) {
                // Cast the long absolute difference back to int safely
                minDiff = Math.min(minDiff, (int) Math.abs((long) leftSums[insertionPoint - 1] + rightSum - goal));
            }
        }
        
        return minDiff;
    }
    
    // Helper function to generate all possible subset sums using bitmasking
    private int[] generateSubsetSums(int[] nums, int start, int end) {
        int length = end - start;
        int totalSubsets = 1 << length;
        int[] sums = new int[totalSubsets];
        
        for (int i = 0; i < totalSubsets; i++) {
            int currentSum = 0;
            for (int j = 0; j < length; j++) {
                if (((i >> j) & 1) == 1) {
                    currentSum += nums[start + j];
                }
            }
            sums[i] = currentSum;
        }
        
        return sums;
    }
}
