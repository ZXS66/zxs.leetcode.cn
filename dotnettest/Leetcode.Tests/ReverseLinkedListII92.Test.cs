namespace Leetcode.Tests;

public class ReverseLinkedListII92Test
{
    [Fact]
    public void ReverseBetween()
    {
        var sln = new Solution92();
        var result1 = sln.ReverseBetween(LeetcodeHelper.CreateList([1, 2, 3, 4, 5]), 2, 4);
        Assert.Equal("[1,4,3,2,5]", LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.ReverseBetween(LeetcodeHelper.CreateList([5]), 1, 1);
        Assert.Equal("[5]", LeetcodeHelper.ListNodeToString(result2));
        var result3 = sln.ReverseBetween(LeetcodeHelper.CreateList([5, 6, 7]), 1, 2);
        Assert.Equal("[6,5,7]", LeetcodeHelper.ListNodeToString(result3));
        var result4 = sln.ReverseBetween(LeetcodeHelper.CreateList([7, 8, 9]), 2, 3);
        Assert.Equal("[7,9,8]", LeetcodeHelper.ListNodeToString(result4));
    }
}

