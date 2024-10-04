// https://leetcode.cn/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150


public class Solution92
{
    public ListNode ReverseBetween(ListNode head, int left, int right)
    {
        ListNode node = head;
        ListNode prevNode = null;
        ListNode nodeBeforeLeft = null;
        ListNode leftNode = null;
        ListNode rightNode = null;
        // both left and right are 1 based number, not 0 based!!!
        // both left and right are inclusive!!!
        int idx = 1;
        while (idx < left)
        {
            prevNode = node;
            node = node.next;
            idx++;
        }
        nodeBeforeLeft = prevNode;
        leftNode = node;
        while (idx <= right)
        {
            var next = node.next;
            if (idx != left)
            {
                node.next = prevNode;
            }
            if (idx == right)
            {
                rightNode = node;
            }
            prevNode = node;
            node = next;
            idx++;
        }
        if (nodeBeforeLeft != null)
        {
            nodeBeforeLeft.next = rightNode;
        }
        leftNode.next = node;
        return nodeBeforeLeft == null ? rightNode : head;
    }
}
