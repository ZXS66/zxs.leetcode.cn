namespace Leetcode.Tests;

public class MaximumDepthOfBinaryTree104Test
{
    [Fact]
    public void MaxDepth()
    {
        var sln = new Solution104();
        var result1 = sln.MaxDepth(LeetcodeHelper.CreateTree([3, 9, 20, null, null, 15, 7]));
        Assert.Equal(3, result1);
        var result2 = sln.MaxDepth(LeetcodeHelper.CreateTree([1, null, 2]));
        Assert.Equal(2, result2);
    }
}
