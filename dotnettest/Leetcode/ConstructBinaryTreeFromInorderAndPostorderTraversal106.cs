// https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150


public class Solution106
{
    public TreeNode BuildTree(int[] inorder, int[] postorder)
    {
        if (postorder.Length == 0) return null;
        TreeNode root = new TreeNode(postorder.Last());
        if (postorder.Length == 1) return root;
        int lengthOfLeft = inorder.ToList().IndexOf(postorder.Last());
        int[] inorderOfLeft = inorder.Take(lengthOfLeft).ToArray();
        int[] postorderOfLeft = postorder.Take(lengthOfLeft).ToArray();
        root.left = BuildTree(inorderOfLeft, postorderOfLeft);
        int[] inorderOfRight = inorder.Skip(lengthOfLeft + 1).ToArray();
        int[] postorderOfRight = postorder.Skip(lengthOfLeft).Take(postorder.Length - lengthOfLeft - 1).ToArray();
        root.right = BuildTree(inorderOfRight, postorderOfRight);
        return root;
    }
}