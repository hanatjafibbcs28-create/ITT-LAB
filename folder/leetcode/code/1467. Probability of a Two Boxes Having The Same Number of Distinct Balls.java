import java.util.Arrays;

public class Solution {
    // A precomputed factorial/combination array can be used, or calculated dynamically
    private double[][] comb;

    public double getProbability(int[] balls) {
        int k = balls.length;
        int totalBalls = 0;
        for (int b : balls) totalBalls += b;
        int n = totalBalls / 2;

        // Precompute combinations up to 48 (max balls possible: 8 * 6 = 48)
        comb = new double[totalBalls + 1][totalBalls + 1];
        for (int i = 0; i <= totalBalls; i++) {
            comb[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        // We track: (colorIndex, ballsInBox1, colorDiff)
        // Since colorDiff can range from -8 to +8, we add an offset of 8 to keep indices non-negative
        Double[][][] memo = new Double[k][n + 1][17];

        double validWays = dfs(0, 0, 0, balls, n, memo);
        double totalWays = comb[totalBalls][n];

        return validWays / totalWays;
    }

    private double dfs(int colorIdx, int count1, int colorDiff, int[] balls, int n, Double[][][] memo) {
        // Base case: processed all colors
        if (colorIdx == balls.length) {
            // Box 1 must have exactly n balls and color difference must be exactly 0
            if (count1 == n && colorDiff == 0) {
                return 1.0;
            }
            return 0.0;
        }

        // Return cached result with colorDiff offset adjustment (+8)
        if (memo[colorIdx][count1][colorDiff + 8] != null) {
            return memo[colorIdx][count1][colorDiff + 8];
        }

        double ways = 0;
        int currentBallCount = balls[colorIdx];

        // Loop through all possible number of balls from this color to put into Box 1
        for (int x = 0; x <= currentBallCount; x++) {
            if (count1 + x > n) break; // Prune if Box 1 exceeds its size capacity n

            // Calculate the impact on color diversity
            int d = 0;
            if (x > 0) d++;                       // Color exists in Box 1
            if (currentBallCount - x > 0) d--;    // Color exists in Box 2

            // Recursively evaluate choices for the next colors
            ways += comb[currentBallCount][x] * dfs(colorIdx + 1, count1 + x, colorDiff + d, balls, n, memo);
        }

        memo[colorIdx][count1][colorDiff + 8] = ways;
        return ways;
    }
}
