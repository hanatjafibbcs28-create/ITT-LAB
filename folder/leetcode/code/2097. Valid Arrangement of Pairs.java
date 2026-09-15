import java.util.*;
class Solution {
    public int[][] validArrangement(int[][] pairs) {
        Map<Integer, Deque<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> outDegree = new HashMap<>();
        Map<Integer, Integer> inDegree = new HashMap<>();
        for (int[] pair : pairs) {
            int u = pair[0];
            int v = pair[1];
            graph.putIfAbsent(u, new ArrayDeque<>());
            graph.get(u).add(v);
            outDegree.put(u, outDegree.getOrDefault(u, 0) + 1);
            inDegree.put(v, inDegree.getOrDefault(v, 0) + 1);
        }
        int startNode = pairs[0][0]; 
        for (int node : graph.keySet()) {
            if (outDegree.getOrDefault(node, 0) - inDegree.getOrDefault(node, 0) == 1) {
                startNode = node;
                break;
            }
        }
        List<Integer> path = new ArrayList<>();
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(startNode);
        while (!stack.isEmpty()) {
            int curr = stack.peek();
            Deque<Integer> neighbors = graph.get(curr);
            if (neighbors != null && !neighbors.isEmpty()) {
                stack.push(neighbors.pollFirst());
            } else {
                path.add(stack.pop());
            }
        }
        int[][] result = new int[pairs.length][2];
        int idx = 0;
        for (int i = path.size() - 1; i > 0; i--) {
            result[idx][0] = path.get(i);
            result[idx][1] = path.get(i - 1);
            idx++;
        }
        return result;
    }
}
