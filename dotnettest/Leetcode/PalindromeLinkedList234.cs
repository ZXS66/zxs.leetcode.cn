// https://leetcode.cn/problems/palindrome-linked-list/?envType=study-plan-v2&envId=top-100-liked

public class Solution234
{
    public bool IsPalindrome(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return true;
        }
        List<int> values = new List<int>();
        ListNode current = head;
        while (current != null)
        {
            values.Add(current.val);
            current = current.next;
        }
        int left = 0;
        int right = values.Count - 1;
        while (left < right)
        {
            if (values[left] != values[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
