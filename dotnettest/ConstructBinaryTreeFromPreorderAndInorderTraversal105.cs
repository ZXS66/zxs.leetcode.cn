// https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150


public class Solution105
{
    public TreeNode BuildTree(int[] preorder, int[] inorder)
    {
        if (preorder.Length == 0) return null;
        TreeNode root = new TreeNode(preorder[0]);
        if (preorder.Length == 1) return root;
        int lengthOfLeft = inorder.ToList().IndexOf(preorder[0]);
        int[] preorderOfLeft = preorder.Skip(1).Take(lengthOfLeft).ToArray();
        int[] inorderOfLeft = inorder.Take(lengthOfLeft).ToArray();
        root.left = BuildTree(preorderOfLeft, inorderOfLeft);
        int[] preorderOfRight = preorder.Skip(lengthOfLeft + 1).ToArray();
        int[] inorderOfRight = inorder.Skip(lengthOfLeft + 1).ToArray();
        root.right = BuildTree(preorderOfRight, inorderOfRight);
        return root;
    }
}


