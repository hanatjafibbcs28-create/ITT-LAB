import java.util.Random;
import java.util.Arrays;
class Solution {
    private int[][] rects;
    private int[] prefixSums;
    private int totalPoints;
    private Random rand;
    public Solution(int[][] rects) {
        this.rects = rects;
        this.rand = new Random();
        this.prefixSums = new int[rects.length];
        this.totalPoints = 0;
        for (int i = 0; i < rects.length; i++) {
            int width = rects[i][2] - rects[i][0] + 1;
            int height = rects[i][3] - rects[i][1] + 1;
            totalPoints += width * height;
            prefixSums[i] = totalPoints;
        }
    }
    public int[] pick() {
        int target = rand.nextInt(totalPoints) + 1;
        int rectIdx = Arrays.binarySearch(prefixSums, target);
        if (rectIdx < 0) {
            rectIdx = -rectIdx - 1;
        }
        int[] rect = rects[rectIdx];
        int width = rect[2] - rect[0] + 1;
        int prevPoints = (rectIdx == 0) ? 0 : prefixSums[rectIdx - 1];
        int offset = target - prevPoints - 1; 
        int u = rect[0] + (offset % width);
        int v = rect[1] + (offset / width);
        return new int[]{u, v};
    }
}
/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
