namespace Leetcode.Tests;

public class LinkedListCycleII142Test
{
    [Fact]
    public void DetectCycle()
    {
        var sln = new Solutoin142();
        var testcase1 = LeetcodeHelper.CreateList([3, 2, 0, -4]);
        testcase1.next.next.next.next = testcase1.next; // Create a cycle
        var result1 = sln.DetectCycle(testcase1);
        Assert.NotNull(result1);
        Assert.Equal(2, result1.val);
        var testcase2 = LeetcodeHelper.CreateList([1, 2]);
        testcase2.next.next = testcase2; // Create a cycle
        var result2 = sln.DetectCycle(testcase2);
        Assert.NotNull(result2);
        Assert.Equal(1, result2.val);
        var testcase3 = LeetcodeHelper.CreateList([1]);
        // testcase3.next = null; // No cycle
        var result3 = sln.DetectCycle(testcase3);
        Assert.Null(result3);
    }
}
