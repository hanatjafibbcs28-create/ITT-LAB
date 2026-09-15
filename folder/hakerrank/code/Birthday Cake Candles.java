import java.io.*;
import java.util.*;

public class Solution {

    public static int birthdayCakeCandles(List<Integer> candles) {
        int maxHeight = Integer.MIN_VALUE;
        int count = 0;
        
        for (int height : candles) {
            if (height > maxHeight) {
                // Found a taller candle: update max and reset counter
                maxHeight = height;
                count = 1;
            } else if (height == maxHeight) {
                // Found another candle matching the max height: increment counter
                count++;
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        List<Integer> candles = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            candles.add(in.nextInt());
        }
        
        int result = birthdayCakeCandles(candles);
        System.out.println(result);
        
        in.close();
    }
}
