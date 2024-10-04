// https://leetcode.cn/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150

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
public class Solution86
{
    public ListNode Partition(ListNode head, int x)
    {
        var dummyLess = new ListNode(0);
        var dummyMore = new ListNode(0);
        var curLess = dummyLess;
        var curMore = dummyMore;
        while (head != null)
        {
            if (head.val < x)
            {
                curLess.next = head;
                curLess = curLess.next;
            }
            else
            {
                curMore.next = head;
                curMore = curMore.next;
            }
            head = head.next;
        }
        curMore.next = null;
        curLess.next = dummyMore.next;
        return dummyLess.next;
    }
}