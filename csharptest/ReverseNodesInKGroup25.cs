// https://leetcode.cn/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150

public class Solution25
{
    public ListNode ReverseKGroup(ListNode head, int k)
    {
        ListNode newHead = null;
        Stack<ListNode> stack = new Stack<ListNode>();
        int idx = 0;
        ListNode cur = null;
        while (head != null)
        {
            stack.Push(head);
            head = head.next;
            idx++;
            if (idx % k == 0)
            {
                while (stack.Count() > 0)
                {
                    ListNode node = stack.Pop();
                    if (newHead == null)
                    {
                        newHead = node;
                    }
                    if (cur != null)
                    {
                        cur.next = node;
                    }
                    cur = node;
                }
                // bug fix: clear left node's next pointer to prevent cycle when the length of the linked list is equals to k.
                cur.next = null;
            }
        }
        if (stack.Count() > 0)
        {
            cur.next = stack.Last();
        }
        return newHead;
    }
}

