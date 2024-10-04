namespace Leetcode.Tests;

public class LengthOfTheLongestAlphabeticalContinuousSubstring2414Test
{
    [Fact]
    public void LongestContinuousSubstring()
    {
        var sln = new Solution2414();
        var result1 = sln.LongestContinuousSubstring("abacaba");
        Assert.Equal(2, result1);
        var result2 = sln.LongestContinuousSubstring("abcde");
        Assert.Equal(5, result2);
    }
}
