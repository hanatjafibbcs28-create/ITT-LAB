import java.io.*;
import java.util.*;

public class Solution {

    public static void plusMinus(List<Integer> arr) {
        int positiveCount = 0;
        int negativeCount = 0;
        int zeroCount = 0;
        int n = arr.size();
        
        // Count frequencies of positive, negative, and zero values
        for (int num : arr) {
            if (num > 0) {
                positiveCount++;
            } else if (num < 0) {
                negativeCount++;
            } else {
                zeroCount++;
            }
        }
        
        // Cast n to double to perform floating-point division
        System.out.printf("%.6f%n", (double) positiveCount / n);
        System.out.printf("%.6f%n", (double) negativeCount / n);
        System.out.printf("%.6f%n", (double) zeroCount / n);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        List<Integer> arr = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            arr.add(in.nextInt());
        }
        
        plusMinus(arr);
        
        in.close();
    }
}
