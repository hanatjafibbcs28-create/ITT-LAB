public class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        int minCost = 0;
        int edgesUsed = 0;
        
        // Track whether a point is already included in the MST
        boolean[] inMST = new boolean[n];
        
        // Stores the minimum distance from the current MST to each point
        int[] minDist = new int[n];
        for (int i = 1; i < n; i++) {
            minDist[i] = Integer.MAX_VALUE;
        }
        
        // Start building the tree from node 0
        minDist[0] = 0;
        
        while (edgesUsed < n) {
            int currNode = -1;
            int currMinDist = Integer.MAX_VALUE;
            
            // Step 1: Find the node with the absolute smallest edge distance to the current MST
            for (int i = 0; i < n; i++) {
                if (!inMST[i] && minDist[i] < currMinDist) {
                    currMinDist = minDist[i];
                    currNode = i;
                }
            }
            
            // Step 2: Include this node into the MST
            inMST[currNode] = true;
            minCost += currMinDist;
            edgesUsed++;
            
            // Step 3: Update the min distance array for all neighboring unvisited nodes
            for (int nextNode = 0; nextNode < n; nextNode++) {
                if (!inMST[nextNode]) {
                    int dist = Math.abs(points[currNode][0] - points[nextNode][0]) 
                             + Math.abs(points[currNode][1] - points[nextNode][1]);
                    
                    if (dist < minDist[nextNode]) {
                        minDist[nextNode] = dist;
                    }
                }
            }
        }
        
        return minCost;
    }
}
