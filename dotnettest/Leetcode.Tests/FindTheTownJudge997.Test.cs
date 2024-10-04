namespace Leetcode.Tests;

public class FindTheTownJudge997Test
{
    [Fact]
    public void FindJudge()
    {
        var sln = new Solution997();
        var result1 = sln.FindJudge(2, [[1, 2]]);
        Assert.Equal(2, result1);
        var result2 = sln.FindJudge(3, [[1, 3], [2, 3]]);
        Assert.Equal(3, result2);
        var result3 = sln.FindJudge(3, [[1, 3], [2, 3], [3, 1]]);
        Assert.Equal(-1, result3);
        var result4 = sln.FindJudge(1, []);
        Assert.Equal(1, result4);
    }
}
