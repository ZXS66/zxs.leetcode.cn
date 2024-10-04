namespace Leetcode.Tests;

public class ReverseNodesInKGroup25Test
{
    [Fact]
    public void ReverseKGroup()
    {
        var sln = new Solution25();
        var result1 = sln.ReverseKGroup(LeetcodeHelper.CreateList([1, 2, 3, 4, 5]), 2);
        Assert.Equal("[2,1,4,3,5]", LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.ReverseKGroup(LeetcodeHelper.CreateList([1, 2, 3, 4, 5]), 3);
        Assert.Equal("[3,2,1,4,5]", LeetcodeHelper.ListNodeToString(result2));
        var result3 = sln.ReverseKGroup(LeetcodeHelper.CreateList([1, 2]), 2);
        Assert.Equal("[2,1]", LeetcodeHelper.ListNodeToString(result3));
    }
}
