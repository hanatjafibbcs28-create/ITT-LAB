import java.io.*;
import java.util.*;

public class Solution {

    public static String timeConversion(String s) {
        // Extract components from the input string (e.g., "07:05:45PM")
        String amPm = s.substring(s.length() - 2); // "PM"
        int hour = Integer.parseInt(s.substring(0, 2)); // 7
        String restOfTime = s.substring(2, s.length() - 2); // ":05:45"
        
        String hourStr;
        
        if (amPm.equals("AM")) {
            if (hour == 12) {
                hourStr = "00"; // 12:00:00AM becomes 00:00:00
            } else {
                hourStr = String.format("%02d", hour); // Keep original AM hour
            }
        } else { // It is PM
            if (hour == 12) {
                hourStr = "12"; // 12:00:00PM stays 12:00:00
            } else {
                hourStr = String.format("%02d", hour + 12); // Add 12 to PM hours
            }
        }
        
        return hourStr + restOfTime;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        String result = timeConversion(s);
        System.out.println(result);
        in.close();
    }
}
