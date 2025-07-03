namespace Leetcode.Tests;

public class PathSumIII437Test
{
    [Fact]
    public void PathSum1()
    {
        var tree = LeetcodeHelper.CreateTree([10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]);
        var result = new Solution437().PathSum(tree, 8);
        Assert.Equal(3, result);
    }
    [Fact]
    public void PathSum2()
    {
        var tree = LeetcodeHelper.CreateTree([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, null, 5, 1]);
        var result = new Solution437().PathSum(tree, 22);
        Assert.Equal(3, result);
    }
    [Fact]
    public void PathSum3()
    {
        var tree = LeetcodeHelper.CreateTree([1, null, 2, null, null, null, 3, null, null, null, null, null, null, null, 4, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 5]);
        var result = new Solution437().PathSum(tree, 3);
        Assert.Equal(2, result);
    }
    [Fact]
    public void PathSum4()
    {
        var tree = LeetcodeHelper.CreateTree([1000000000, 1000000000, null, 294967296, null, null, null, 1000000000, null, null, null, null, null, null, null, 1000000000, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 1000000000]);
        var result = new Solution437().PathSum(tree, 0);
        Assert.Equal(0, result);
    }
}