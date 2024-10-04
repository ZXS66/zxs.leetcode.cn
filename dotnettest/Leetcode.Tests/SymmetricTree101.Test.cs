namespace Leetcode.Tests;

public class SymmetricTree101Test
{
    [Fact]
    public void NthPersonGetsNthSeat()
    {
        var sln = new Solution101();
        var result1 = sln.IsSymmetric(LeetcodeHelper.CreateTree([1, 2, 2, 3, 4, 4, 3]));
        Assert.True(result1);
        var result2 = sln.IsSymmetric(LeetcodeHelper.CreateTree([1, 2, 2, null, 3, null, 3]));
        Assert.False(result2);
    }
}
