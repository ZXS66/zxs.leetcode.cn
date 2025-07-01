// https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked


public class Solution206
{
    public ListNode ReverseList(ListNode head)
    {
        ListNode prev = null;
        ListNode current = head;
        while (current != null)
        {
            ListNode nextTemp = current.next; // Store the next node
            current.next = prev;              // Reverse the link
            prev = current;                   // Move prev to current
            current = nextTemp;               // Move to the next node
        }
        return prev; // New head of the reversed list        
    }
}
