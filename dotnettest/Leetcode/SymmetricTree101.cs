// https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150

public class Solution101
{
    public bool IsSymmetric(TreeNode root)
    {
        if (root == null || (root.left == null && root.right == null)) return true;
        if (root.left?.val != root.right?.val) return false;
        return isSameTreeNode(root.left, root.right);
    }

    private bool isSameTreeNode(TreeNode p, TreeNode q)
    {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        return p.val == q.val && isSameTreeNode(p.left, q.right) && isSameTreeNode(p.right, q.left);
    }
}