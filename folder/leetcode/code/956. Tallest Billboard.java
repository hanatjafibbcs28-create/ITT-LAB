import java.util.Arrays;

public class Solution {
    public int tallestBillboard(int[] rods) {
        int sum = 0;
        for (int rod : rods) {
            sum += rod;
        }

        // dp[d] stores the maximum height of the taller support given a difference 'd'
        // Initialize all values to -1 (unreachable states)
        int[] dp = new int[sum + 1];
        Arrays.fill(dp, -1);
        dp[0] = 0; // Base case: 0 difference means 0 height for both supports

        for (int rod : rods) {
            // Create a copy of the current DP array to avoid using the same rod multiple times
            int[] currentDp = dp.clone();

            for (int d = 0; d <= sum; d++) {
                if (currentDp[d] == -1) continue;

                // Choice 1: Add rod to the taller support
                // The difference increases by `rod`. The new taller height grows by `rod`.
                if (d + rod <= sum) {
                    dp[d + rod] = Math.max(dp[d + rod], currentDp[d] + rod);
                }

                // Choice 2: Add rod to the shorter support
                // The new difference becomes the absolute value of (d - rod)
                int newDiff = Math.abs(d - rod);
                // The new taller support height is either the previous taller height (if it stayed taller)
                // or the new shifted taller height (if the shorter support overtook the taller one).
                int newTaller = Math.max(currentDp[d], currentDp[d] - d + rod);
                
                dp[newDiff] = Math.max(dp[newDiff], newTaller);
            }
        }

        // The answer is the maximum height where the difference between supports is exactly 0
        return dp[0];
    }
}
