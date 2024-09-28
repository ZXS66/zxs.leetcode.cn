
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



/// <summary>Definition for a binary tree node.</summary>
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/// <summary>
/// definition for binary tree with next pointer that points to the next node in the same level
/// </summary>
public class BinaryNodeWithNextPointer {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public BinaryNodeWithNextPointer() {}

    public BinaryNodeWithNextPointer(int _val) {
        val = _val;
    }

    public BinaryNodeWithNextPointer(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}