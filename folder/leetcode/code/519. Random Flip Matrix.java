import java.util.HashMap;
import java.util.Map;
import java.util.Random;
class Solution {
    private int rows;
    private int cols;
    private int total;
    private Map<Integer, Integer> map;
    private Random rand;
    public Solution(int m, int n) {
        this.rows = m;
        this.cols = n;
        this.rand = new Random();
        reset();
    }
    public int[] flip() {
        int idx = rand.nextInt(total);
        int target = map.getOrDefault(idx, idx);
        int lastElement = map.getOrDefault(total - 1, total - 1);
        map.put(idx, lastElement);
        total--;
        return new int[]{target / cols, target % cols};
    }
    public void reset() {
        this.map = new HashMap<>();
        this.total = this.rows * this.cols;
    }
}
/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(m, n);
 * int[] param_1 = obj.flip();
 * obj.reset();
 */
