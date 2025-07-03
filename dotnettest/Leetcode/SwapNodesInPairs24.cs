// https://leetcode.cn/problems/swap-nodes-in-pairs/description/?envType=study-plan-v2&envId=top-100-liked
public class Solution24 {
    public ListNode SwapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode newHead = head.next;
        head.next = SwapPairs(newHead.next);
        newHead.next = head;

        return newHead;
    }
}