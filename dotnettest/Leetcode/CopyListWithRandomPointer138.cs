// https://leetcode.cn/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150

public class Solution138
{
    public Node? CopyRandomList(Node head)
    {
        if (head == null) return null;
        Node deepHead = new Node(head.val);
        Node headCur = head;
        Node deepCur = deepHead;
        List<Node> headList = new List<Node>() { headCur };
        List<Node> deepList = new List<Node>() { deepCur };
        while (headCur.next != null)
        {
            // set next Node
            deepCur.next = new Node(headCur.next.val);
            deepList.Add(deepCur.next);
            deepCur = deepCur.next;
            headList.Add(headCur.next);
            headCur = headCur.next;
        }
        headCur = head;
        deepCur = deepHead;
        while (headCur != null)
        {
            // set random Node
            if (headCur.random != null)
            {
                deepCur.random = deepList[headList.IndexOf(headCur.random)];
            }
            deepCur = deepCur.next;
            headCur = headCur.next;
        }
        return deepHead;
    }
}
