namespace Leetcode.Tests;

public class RemoveDuplicatesFromSortedListII82Test
{
    [Fact]
    public void DeleteDuplicates()
    {
        var sln = new Solution82();
        var result1 = sln.DeleteDuplicates(LeetcodeHelper.CreateList([1, 2, 3, 3, 4, 4, 5]));
        Assert.Equal("[1,2,5]",LeetcodeHelper.ListNodeToString(result1));
        var result2 = sln.DeleteDuplicates(LeetcodeHelper.CreateList([1, 1, 1, 2, 3]));
        Assert.Equal("[2,3]",LeetcodeHelper.ListNodeToString(result2));
        var result3 = sln.DeleteDuplicates(LeetcodeHelper.CreateList([1, 1]));
        Assert.Equal("[]",LeetcodeHelper.ListNodeToString(result3));
    }
}
