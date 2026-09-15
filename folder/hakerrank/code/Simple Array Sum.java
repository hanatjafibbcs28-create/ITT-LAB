import java.io.*;
import java.util.*;

public class Solution {

    public static int simpleArraySum(List<Integer> ar) {
        int sum = 0;
        // Iterate through the list and add each element to the running total
        for (int num : ar) {
            sum += num;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        // Read the size of the array
        int n = in.nextInt();
        List<Integer> ar = new ArrayList<>();
        
        // Read each space-separated integer into the list
        for (int i = 0; i < n; i++) {
            ar.add(in.nextInt());
        }
        
        // Compute and print the final sum
        int result = simpleArraySum(ar);
        System.out.println(result);
        
        in.close();
    }
}
