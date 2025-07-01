namespace Leetcode.Tests;

public class Solution206Test
{
    [Fact]
    public ListNode ReverseList()
    {
        var sln = new Solution206();
        var result1 = sln.ReverseList(LeetcodeHelper.CreateList([1, 2, 3, 4, 5]));
        Assert.Equal("[5,4,3,2,1]", LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.ReverseList(LeetcodeHelper.CreateList([5]));
        Assert.Equal("[5]", LeetcodeHelper.ListNodeToString(result2));
        var result3 = sln.ReverseList(LeetcodeHelper.CreateList([5, 6, 7]));
        Assert.Equal("[7,6,5]", LeetcodeHelper.ListNodeToString(result3));
        var result4 = sln.ReverseList(LeetcodeHelper.CreateList([7, 8, 9]));
        Assert.Equal("[9,8,7]", LeetcodeHelper.ListNodeToString(result4));
        return result1;
    }
}
