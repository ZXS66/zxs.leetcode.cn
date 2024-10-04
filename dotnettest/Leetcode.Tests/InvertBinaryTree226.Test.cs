namespace Leetcode.Tests;

public class InvertBinaryTree226Test
{
    [Fact]
    public void InvertTree()
    {
        var sln = new Solution226();
        var result1 = sln.InvertTree(LeetcodeHelper.CreateTree([4, 2, 7, 1, 3, 6, 9]));
        Assert.Equal("4,7,2,9,6,3,1", LeetcodeHelper.TreeToString(result1));
        var result2 = sln.InvertTree(LeetcodeHelper.CreateTree([2, 1, 3]));
        Assert.Equal("2,3,1", LeetcodeHelper.TreeToString(result2));
        var result3 = sln.InvertTree(LeetcodeHelper.CreateTree([]));
        Assert.Equal("null", LeetcodeHelper.TreeToString(result3));
    }
}

