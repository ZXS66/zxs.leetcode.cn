// https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150


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
public class Solution19
{
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        ListNode nthNode = head;
        ListNode nthNodeBefore = null;
        ListNode cur = head;
        int i = 0;
        while (i < n)
        {
            cur = cur.next;
            i++;
        }
        while (cur != null)
        {
            nthNodeBefore = nthNode;
            nthNode = nthNode.next;
            cur = cur.next;
            i++;
        }
        if (nthNodeBefore != null)
        {
            nthNodeBefore.next = nthNode.next;
            return head;
        }
        else
        {
            // edge case: the length of linked list is equals to n
            return nthNode.next;
        }
    }
}
