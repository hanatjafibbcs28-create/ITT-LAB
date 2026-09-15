import java.io.*;
import java.util.*;

public class Solution {

    public static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
        int aliceScore = 0;
        int bobScore = 0;
        
        // Loop exactly 3 times since the input structures are always triplets
        for (int i = 0; i < 3; i++) {
            if (a.get(i) > b.get(i)) {
                aliceScore++;
            } else if (a.get(i) < b.get(i)) {
                bobScore++;
            }
        }
        
        // Return a list containing Alice's score followed by Bob's score
        return Arrays.asList(aliceScore, bobScore);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        List<Integer> a = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            a.add(in.nextInt());
        }
        
        List<Integer> b = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            b.add(in.nextInt());
        }
        
        List<Integer> result = compareTriplets(a, b);
        
        // Print the result separated by a space
        System.out.println(result.get(0) + " " + result.get(1));
        
        in.close();
    }
}
