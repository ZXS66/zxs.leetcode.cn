namespace Leetcode.Tests;

public class RemoveNthNodeFromEndOfList19Test
{
    [Fact]
    public void RemoveNthFromEnd()
    {
        var sln = new Solution19();
        var result1 = sln.RemoveNthFromEnd(LeetcodeHelper.CreateList([1, 2, 3, 4, 5]), 2);
        Assert.Equal("[1,2,3,5]", LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.RemoveNthFromEnd(LeetcodeHelper.CreateList([1]), 1);
        Assert.Equal("[]", LeetcodeHelper.ListNodeToString(result2));
        var result3 = sln.RemoveNthFromEnd(LeetcodeHelper.CreateList([1, 2]), 1);
        Assert.Equal("[1]", LeetcodeHelper.ListNodeToString(result3));
        var result4 = sln.RemoveNthFromEnd(LeetcodeHelper.CreateList([1, 2]), 2);
        Assert.Equal("[2]", LeetcodeHelper.ListNodeToString(result4));
    }
}
