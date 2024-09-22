// https://leetcode.cn/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150

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
public class Solution61
{
    public ListNode RotateRight(ListNode head, int k)
    {
        if (head == null || head.next == null || k == 0)
        {
            return head;
        }
        List<ListNode> nodes = new List<ListNode>();
        while (head != null)
        {
            nodes.Add(head);
            head = head.next;
        }
        int n = nodes.Count;
        k %= n;
        if (k == 0)
        {
            return nodes[0];
        }
        nodes[n - 1].next = nodes[0];
        nodes[n - k - 1].next = null;
        return nodes[n - k];
    }
}
