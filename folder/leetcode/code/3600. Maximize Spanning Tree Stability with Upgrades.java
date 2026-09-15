import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int maxStability(int n, int[][] edges, int k) {
        List<int[]> mustEdges = new ArrayList<>();
        List<int[]> optionalEdges = new ArrayList<>();

        for (int[] edge : edges) {
            if (edge[3] == 1) {
                mustEdges.add(edge);
            } else {
                optionalEdges.add(edge);
            }
        }

        // Hint 5 & 3: Initial check to ensure mandatory edges don't form a cycle
        DSU initialDsu = new DSU(n);
        for (int[] edge : mustEdges) {
            if (!initialDsu.union(edge[0], edge[1])) {
                return -1; // Mandatory edges contain a cycle, impossible to form a tree
            }
        }

        // Hint 2: Binary search on the maximum possible stability score
        int low = 1;
        int high = 200000; // Capped at 2 * 10^5 since max strength is 10^5 and can double once
        int ans = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isValid(n, mustEdges, optionalEdges, k, mid)) {
                ans = mid;
                low = mid + 1; // Try to find a larger minimum stability
            } else {
                high = mid - 1; // Target stability too high, lower the bound
            }
        }

        return ans;
    }

    // Hint 3: Feasibility checker for a given stability threshold X
    private boolean isValid(int n, List<int[]> mustEdges, List<int[]> optionalEdges, int k, int X) {
        DSU dsu = new DSU(n);
        int edgeCount = 0;

        // 1. All mandatory edges must be capable of reaching strength X
        for (int[] edge : mustEdges) {
            if (edge[2] < X) return false; 
            dsu.union(edge[0], edge[1]);
            edgeCount++;
        }

        // 2. Greedily add optional edges that require 0 upgrades
        for (int[] edge : optionalEdges) {
            if (edge[2] >= X) {
                if (dsu.union(edge[0], edge[1])) {
                    edgeCount++;
                }
            }
        }

        // 3. Greedily add optional edges that require 1 upgrade
        int upgradesUsed = 0;
        for (int[] edge : optionalEdges) {
            if (edge[2] < X && 2 * edge[2] >= X) {
                if (dsu.union(edge[0], edge[1])) {
                    edgeCount++;
                    upgradesUsed++;
                    if (upgradesUsed > k) return false; // Exceeded maximum allowable upgrades
                }
            }
        }

        // Hint 5: Must form a single connected component containing exactly n - 1 edges
        return edgeCount == n - 1;
    }

    // Hint 4: DSU implementation with path compression
    class DSU {
        int[] parent;

        public DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        public int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]); // Path compression
        }

        public boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) {
                parent[rootI] = rootJ;
                return true;
            }
            return false;
        }
    }
}
