// https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked

public class Solution543
{
    public int DiameterOfBinaryTree(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        int diameter = 0;
        int Depth(TreeNode node)
        {
            if (node == null)
            {
                return 0;
            }
            int leftDepth = Depth(node.left);
            int rightDepth = Depth(node.right);
            diameter = Math.Max(diameter, leftDepth + rightDepth);
            return Math.Max(leftDepth, rightDepth) + 1;
        }
        Depth(root);
        return diameter;
    }
}