import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {
    public int minimumDifference(int[] nums) {
        int len = nums.length;
        int n = len / 2;
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // Generate subsets for left and right halves
        // leftSums[k] stores all possible sums using exactly 'k' elements
        List<Integer>[] leftSums = new ArrayList[n + 1];
        List<Integer>[] rightSums = new ArrayList[n + 1];
        
        for (int i = 0; i <= n; i++) {
            leftSums[i] = new ArrayList<>();
            rightSums[i] = new ArrayList<>();
        }

        // Populate lists using bitmasking
        int totalCombinations = 1 << n;
        for (int i = 0; i < totalCombinations; i++) {
            int leftCount = 0, rightCount = 0;
            int leftSum = 0, rightSum = 0;

            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 1) {
                    leftCount++;
                    leftSum += nums[j];

                    rightCount++;
                    rightSum += nums[n + j];
                }
            }
            leftSums[leftCount].add(leftSum);
            rightSums[rightCount].add(rightSum);
        }

        // Sort all lists in rightSums to allow Binary Search
        for (int i = 0; i <= n; i++) {
            Collections.sort(rightSums[i]);
        }

        int minDiff = Integer.MAX_VALUE;

        // Iterate through all possible counts of elements chosen from the left half
        for (int k = 0; k <= n; k++) {
            List<Integer> leftList = leftSums[k];
            List<Integer> rightList = rightSums[n - k]; // Must pick exactly (n - k) from the right half

            for (int leftSum : leftList) {
                // Ideal value for the other subset sum is totalSum / 2
                // So ideal rightSum = (totalSum / 2) - leftSum
                double idealRight = (double) totalSum / 2.0 - leftSum;

                // Binary search for the closest value in rightList
                int low = 0, high = rightList.size() - 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    int currentRightSum = rightList.get(mid);
                    
                    int currentSubsetSum = leftSum + currentRightSum;
                    int currentDiff = Math.abs(totalSum - 2 * currentSubsetSum);
                    minDiff = Math.min(minDiff, currentDiff);

                    if (currentRightSum < idealRight) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
            }
        }

        return minDiff;
    }
}
