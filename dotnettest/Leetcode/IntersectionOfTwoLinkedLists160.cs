// https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked

public class Solution160
{
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        var dumpA = headA;
        var dumpB = headB;
        while (dumpA != dumpB)
        {
            dumpA = dumpA != null ? dumpA.next : headB;
            dumpB = dumpB != null ? dumpB.next : headA;
        }
        return dumpA;
    }
}