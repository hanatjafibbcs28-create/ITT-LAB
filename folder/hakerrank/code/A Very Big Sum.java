import java.io.*;
import java.util.*;

public class Solution {

    // The method return type and parameters must use Long to prevent overflow
    public static long aVeryBigSum(List<Long> ar) {
        long sum = 0;
        
        for (long num : ar) {
            sum += num;
        }
        
        return sum;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        // Read the size of the array
        int n = in.nextInt();
        List<Long> ar = new ArrayList<>();
        
        // Read each space-separated element as a long integer
        for (int i = 0; i < n; i++) {
            ar.add(in.nextLong());
        }
        
        // Compute and print the final 64-bit sum
        long result = aVeryBigSum(ar);
        System.out.println(result);
        
        in.close();
    }
}
