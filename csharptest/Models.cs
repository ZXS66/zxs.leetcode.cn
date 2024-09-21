
/// <summary>
/// Definition for a Node.
/// </summary>
public class Node
{
    public int val;
    public Node? next;
    public Node? random;

    public Node(int _val)
    {
        val = _val;
        next = null;
        random = null;
    }
}



//// <summary>
/// Definition for singly-linked list.
/// </summary>
public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}


