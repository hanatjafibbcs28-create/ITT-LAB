import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

class Solution {
    // Map each unique number to a list of its indices
    private Map<Integer, List<Integer>> indicesMap;
    private Random rand;

    public Solution(int[] nums) {
        this.indicesMap = new HashMap<>();
        this.rand = new Random();
        
        // Pre-process the array to group indices by their value
        for (int i = 0; i < nums.length; i++) {
            this.indicesMap.putIfAbsent(nums[i], new ArrayList<>());
            this.indicesMap.get(nums[i]).add(i);
        }
    }
    
    public int pick(int target) {
        List<Integer> indices = this.indicesMap.get(target);
        
        // Randomly select one index from the list of valid indices
        int randomIndex = rand.nextInt(indices.size());
        return indices.get(randomIndex);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
