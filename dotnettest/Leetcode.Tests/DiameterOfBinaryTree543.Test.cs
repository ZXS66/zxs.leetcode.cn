namespace Leetcode.Tests;

public class DiameterOfBinaryTree543Test
{
    [Fact]
    public void DiameterOfBinaryTreeTest()
    {
        var solution = new Solution543();
        var root = LeetcodeHelper.CreateTree([1, 2, 3, 4, 5]);
        var result = solution.DiameterOfBinaryTree(root);
        Assert.Equal(3, result);
    }

    [Fact]
    public void DiameterOfBinaryTreeTest2()
    {
        var solution = new Solution543();
        var root = LeetcodeHelper.CreateTree([1, 2]);
        var result = solution.DiameterOfBinaryTree(root);
        Assert.Equal(1, result);
    }
}