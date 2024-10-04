namespace Leetcode.Tests;

public class ConstructBinaryTreeFromInorderAndPostorderTraversal106Test
{
    [Fact]
    public void BuildTree()
    {
        var sln = new Solution106();
        var result1 = sln.BuildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]);
        Assert.Equal("3,9,20,null,null,15,7", LeetcodeHelper.TreeToString(result1));
        var result2 = sln.BuildTree([-1], [-1]);
        Assert.Equal("-1", LeetcodeHelper.TreeToString(result2));
    }
}

