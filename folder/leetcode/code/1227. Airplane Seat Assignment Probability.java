public class Solution {
    public double nthPersonGetsNthSeat(int n) {
        // Base case: If there is only 1 passenger, they will always get their own seat.
        if (n == 1) {
            return 1.0;
        }
        // For any number of passengers greater than or equal to 2, the probability is always 0.5
        return 0.5;
    }
}
