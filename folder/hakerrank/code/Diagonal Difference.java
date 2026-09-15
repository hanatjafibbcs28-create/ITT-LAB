import java.io.*;
import java.util.*;

public class Solution {

    public static int diagonalDifference(List<List<Integer>> arr) {
        int primaryDiagonalSum = 0;
        int secondaryDiagonalSum = 0;
        int n = arr.size();
        
        // Single pass layout collects both diagonals simultaneously
        for (int i = 0; i < n; i++) {
            // Primary diagonal element is always at index [i][i]
            primaryDiagonalSum += arr.get(i).get(i);
            
            // Secondary diagonal element is at index [i][n - 1 - i]
            secondaryDiagonalSum += arr.get(i).get(n - 1 - i);
        }
        
        // Return the absolute difference using Math.abs
        return Math.abs(primaryDiagonalSum - secondaryDiagonalSum);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        List<List<Integer>> arr = new ArrayList<>();
        
        // Build the 2D Matrix structure
        for (int i = 0; i < n; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(in.nextInt());
            }
            arr.add(row);
        }
        
        int result = diagonalDifference(arr);
        System.out.println(result);
        
        in.close();
    }
}
