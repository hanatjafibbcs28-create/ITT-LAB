import java.util.Random;
class Solution {
    private ListNode head;
    private Random rand;
    public Solution(ListNode head) {
        this.head = head;
        this.rand = new Random();
    }
    public int getRandom() {
        ListNode curr = this.head;
        int result = curr.val;
        int count = 1;
        while (curr != null) {
            if (rand.nextInt(count) == 0) {
                result = curr.val;
            }
            count++;
            curr = curr.next;
        }
        return result;
    }
}
