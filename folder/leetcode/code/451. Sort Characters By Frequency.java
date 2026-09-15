import java.util.ArrayList;
import java.util.List;

public class Solution {
    public String frequencySort(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }

        // Step 1: Count frequency of each character
        // Using an ASCII/Extended array size 128 covers all English letters and digits
        int[] freqMap = new int[128];
        for (int i = 0; i < s.length(); i++) {
            freqMap[s.charAt(i)]++;
        }

        // Step 2: Create buckets where index = character frequency
        List<Character>[] buckets = new List[s.length() + 1];
        for (int i = 0; i < 128; i++) {
            int freq = freqMap[i];
            if (freq > 0) {
                if (buckets[freq] == null) {
                    buckets[freq] = new ArrayList<>();
                }
                buckets[freq].add((char) i);
            }
        }

        // Step 3: Accumulate the characters from the highest frequency to the lowest
        StringBuilder sb = new StringBuilder();
        for (int freq = buckets.length - 1; freq > 0; freq--) {
            if (buckets[freq] != null) {
                for (char c : buckets[freq]) {
                    // Append character 'freq' times
                    for (int i = 0; i < freq; i++) {
                        sb.append(c);
                    }
                }
            }
        }

        return sb.toString();
    }
}
