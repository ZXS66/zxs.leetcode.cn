// https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked

public class Solution94
{
    public IList<int> InorderTraversal(TreeNode root)
    {
        var result = new List<int>();
        InorderTraversalHelper(root, result);
        return result;
    }

    private void InorderTraversalHelper(TreeNode node, List<int> result)
    {
        if (node == null) return;
        InorderTraversalHelper(node.left, result);
        result.Add(node.val);
        InorderTraversalHelper(node.right, result);
    }
}