namespace Leetcode.Tests;

public class MoveZeros283Test
{
    [Fact]
    public void MoveZeroes()
    {
        var sln = new MoveZeros283();
        int[] input1 = [0, 1, 0, 3, 12];
        sln.MoveZeroes(input1);
        Assert.Equal("[1,3,12,0,0]", LeetcodeHelper.Array2String(input1));
        int[] input2 = [0];
        sln.MoveZeroes(input2);
        Assert.Equal("[0]", LeetcodeHelper.Array2String(input2));
        int[] input3 = [1, 0];
        sln.MoveZeroes(input3);
        Assert.Equal("[1,0]", LeetcodeHelper.Array2String(input3));
    }
}