namespace Leetcode.Tests;

public class SwapNodesInPares24Test
{
    [Fact]
    public void SwapPairsTest()
    {
        var solution = new Solution24();
        // var head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        var head = LeetcodeHelper.CreateList([1,2,3,4]);
        var result = solution.SwapPairs(head);
        Assert.Equal(2, result.val);
        Assert.Equal(1, result.next.val);
        Assert.Equal(4, result.next.next.val);
        Assert.Equal(3, result.next.next.next.val);
        Assert.Null(result.next.next.next.next);
    }
}