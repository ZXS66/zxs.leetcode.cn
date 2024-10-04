namespace Leetcode.Tests;

public class RotateList61Test
{
    [Fact]
    public void RotateRight()
    {
        var sln = new Solution61();
        var result1 = sln.RotateRight(LeetcodeHelper.CreateList([1, 2, 3, 4, 5]), 2);
        Assert.Equal("[4,5,1,2,3]", LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.RotateRight(LeetcodeHelper.CreateList([0, 1, 2]), 4);
        Assert.Equal("[2,0,1]", LeetcodeHelper.ListNodeToString(result2));
    }
}
