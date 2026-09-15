public class Solution {
    public double soupServings(int n) {
        // If n is large, the probability that A empties first is practically 1.0
        if (n >= 4800) {
            return 1.0;
        }
        
        // Scale down the units by dividing by 25 (rounding up)
        int m = (n + 24) / 25;
        
        // dp[i][j] stores the result for i units of soup A and j units of soup B
        double[][] memo = new double[m + 1][m + 1];
        
        return calculate(m, m, memo);
    }
    
    private double calculate(int a, int b, double[][] memo) {
        // Base Cases
        if (a <= 0 && b <= 0) return 0.5; // Both empty at the same time (1.0 * 0.5)
        if (a <= 0) return 1.0;           // Soup A empty first
        if (b <= 0) return 0.0;           // Soup B empty first
        
        // Return cached result if already calculated
        if (memo[a][b] > 0) return memo[a][b];
        
        // Calculate the average probability across all 4 independent paths
        memo[a][b] = 0.25 * (
            calculate(a - 4, b, memo) +     // Option 1: 100mL A, 0mL B
            calculate(a - 3, b - 1, memo) + // Option 2: 75mL A, 25mL B
            calculate(a - 2, b - 2, memo) + // Option 3: 50mL A, 50mL B
            calculate(a - 1, b - 3, memo)   // Option 4: 25mL A, 75mL B
        );
        
        return memo[a][b];
    }
}
