import java.io.*;
import java.util.*;

public class Solution {

    public static void miniMaxSum(List<Integer> arr) {
        long totalSum = 0;
        long minVal = Long.MAX_VALUE;
        long maxVal = Long.MIN_VALUE;
        
        for (int num : arr) {
            totalSum += num;
            if (num < minVal) {
                minVal = num;
            }
            if (num > maxVal) {
                maxVal = num;
            }
        }
        
        // Calculate the min sum by excluding the largest number
        long minSum = totalSum - maxVal;
        // Calculate the max sum by excluding the smallest number
        long maxSum = totalSum - minVal;
        
        System.out.println(minSum + " " + maxSum);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<Integer> arr = new ArrayList<>();
        
        // The problem states there are exactly 5 integers
        for (int i = 0; i < 5; i++) {
            arr.add(in.nextInt());
        }
        
        miniMaxSum(arr);
        in.close();
    }
}
