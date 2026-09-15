import java.io.*;
import java.util.*;

public class Solution {

    public static void staircase(int n) {
        // Loop through each row of the staircase
        for (int i = 1; i <= n; i++) {
            
            // Print n - i spaces for right alignment
            for (int j = 0; j < n - i; j++) {
                System.out.print(" ");
            }
            
            // Print i hash symbols for the step
            for (int j = 0; j < i; j++) {
                System.out.print("#");
            }
            
            // Move to the next row
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        staircase(n);
        in.close();
    }
}
