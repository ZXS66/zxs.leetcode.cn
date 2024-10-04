namespace Leetcode.Tests;

public class SameTree100Test
{
    [Fact]
    public void IsSameTree()
    {
        var sln = new Solution100();
        var result1 = sln.IsSameTree(LeetcodeHelper.CreateTree([1, 2, 3]), LeetcodeHelper.CreateTree([1, 2, 3]));
        Assert.True(result1);
        var result2 = sln.IsSameTree(LeetcodeHelper.CreateTree([1, 2]), LeetcodeHelper.CreateTree([1, null, 2]));
        Assert.False(result2);
        var result3 = sln.IsSameTree(LeetcodeHelper.CreateTree([1, 2, 1]), LeetcodeHelper.CreateTree([1, 1, 2]));
        Assert.False(result3);
    }
}
