namespace Leetcode.Tests;

public class PartitionList86Test
{
    [Fact]
    public void Partition()
    {
        var sln = new Solution86();
        var result1 = sln.Partition(LeetcodeHelper.CreateList([1, 4, 3, 2, 5, 2]), 3);
        Assert.Equal("[1,2,2,4,3,5]", LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.Partition(LeetcodeHelper.CreateList([2, 1]), 2);
        Assert.Equal("[1,2]", LeetcodeHelper.ListNodeToString(result2));
    }
}
