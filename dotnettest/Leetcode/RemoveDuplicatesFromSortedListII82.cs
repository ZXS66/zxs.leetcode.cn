// https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution82
{
    public ListNode DeleteDuplicates(ListNode head)
    {
        ListNode cur = new ListNode { next = head };
        ListNode newHead = cur;
        while (cur.next != null && cur.next.next != null)
        {
            int val = cur.next.val;
            if (val == cur.next.next.val)
            {
                while (cur.next != null && cur.next.val == val)
                {
                    cur.next = cur.next.next;
                }
            }
            else
            {
                cur = cur.next;
            }
        }
        return newHead.next;
    }
}