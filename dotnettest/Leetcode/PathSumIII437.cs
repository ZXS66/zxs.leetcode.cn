// https://leetcode.cn/problems/path-sum-iii/description/?envType=study-plan-v2&envId=top-100-liked

public class Solution437
{
    public int PathSum(TreeNode root, int targetSum)
    {
        if (root == null)
        {
            return 0;
        }
        int ans = dfs(root, targetSum);
        ans += PathSum(root.left, targetSum);
        ans += PathSum(root.right, targetSum);
        return ans;
    }
    private int dfs(TreeNode node, long sum)
    {
        if (node == null)
        {
            return 0;
        }
        int count = node.val == sum ? 1 : 0;
        count += dfs(node.left, sum - node.val);
        count += dfs(node.right, sum - node.val);
        return count;
    }
}