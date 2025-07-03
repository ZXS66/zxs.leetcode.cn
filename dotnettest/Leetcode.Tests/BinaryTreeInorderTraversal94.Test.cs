namespace Leetcode.Tests;

public class BinaryTreeInorderTraversal94Test
{
    [Fact]
    public void InorderTraversalTest()
    {
        var solution = new Solution94();
        var root = LeetcodeHelper.CreateTree([1, null, 2, null, null, 3]);
        var result = solution.InorderTraversal(root);
        Assert.Equal("[1,3,2]", LeetcodeHelper.Array2String(result.ToArray()));
    }
}