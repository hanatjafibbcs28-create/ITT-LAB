import java.io.*;
import java.util.*;

public class Solution {

    public static int solveMeFirst(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        // Fixed: Changed System.util.in to System.in
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int sum = solveMeFirst(a, b);
        System.out.println(sum);
        in.close();
    }
}
