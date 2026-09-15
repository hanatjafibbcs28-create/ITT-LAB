public class Solution {
    public double[] sampleStats(int[] count) {
        double min = -1;
        double max = -1;
        double mean = 0;
        double median = 0;
        double mode = 0;

        long totalCount = 0;
        long totalSum = 0;
        int maxFreq = 0;

        // Step 1: Compute Total Count, Sum, Min, Max, and Mode
        for (int i = 0; i < 256; i++) {
            if (count[i] > 0) {
                if (min == -1) {
                    min = i; // First element with count > 0 is the min
                }
                max = i; // Continually update to find the last non-zero count element (max)
                
                totalCount += count[i];
                totalSum += (long) i * count[i];

                if (count[i] > maxFreq) {
                    maxFreq = count[i];
                    mode = i;
                }
            }
        }

        mean = (double) totalSum / totalCount;

        // Step 2: Compute Median
        // We find the elements at position (totalCount - 1) / 2 and totalCount / 2 (0-indexed)
        long medianIdx1 = (totalCount - 1) / 2;
        long medianIdx2 = totalCount / 2;
        
        long currentCount = 0;
        double m1 = -1, m2 = -1;

        for (int i = 0; i < 256; i++) {
            if (count[i] > 0) {
                currentCount += count[i];
                
                if (m1 == -1 && currentCount > medianIdx1) {
                    m1 = i;
                }
                if (m2 == -1 && currentCount > medianIdx2) {
                    m2 = i;
                    break; // Both midpoints found, we can terminate early
                }
            }
        }

        median = (m1 + m2) / 2.0;

        return new double[]{min, max, mean, median, mode};
    }
}
