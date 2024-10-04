// https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

public class Solution226
{
    public TreeNode InvertTree(TreeNode root)
    {
        if (root == null) return null;
        var temp = root.left;
        root.left = root.right;
        root.right = temp;
        InvertTree(root.left);
        InvertTree(root.right);
        return root;
    }
}