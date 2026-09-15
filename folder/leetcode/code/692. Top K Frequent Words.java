import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // Step 1: Count frequency of each word
        Map<String, Integer> countMap = new HashMap<>();
        for (String word : words) {
            countMap.put(word, countMap.getOrDefault(word, 0) + 1);
        }

        // Step 2: Build a Min-Heap of size k
        // If frequencies are equal, sort lexicographically in descending order (b.compareTo(a))
        // Otherwise, sort by frequency in ascending order (a - b)
        PriorityQueue<String> minHeap = new PriorityQueue<>((w1, w2) -> {
            int freq1 = countMap.get(w1);
            int freq2 = countMap.get(w2);
            if (freq1 == freq2) {
                return w2.compareTo(w1); 
            }
            return freq1 - freq2;
        });

        // Step 3: Maintain only the top k elements in the heap
        for (String word : countMap.keySet()) {
            minHeap.add(word);
            if (minHeap.size() > k) {
                minHeap.poll(); // Evict the least frequent or lexicographically lower element
            }
        }

        // Step 4: Extract elements from the heap into a result list
        List<String> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            result.add(minHeap.poll());
        }

        // Since it's a min-heap, elements were extracted from smallest to largest.
        // Reverse it to get descending order of frequency.
        Collections.reverse(result);
        return result;
    }
}
