namespace Leetcode.Tests;

public class PalindromeLinkedList234Test
{
    [Fact]
    public void IsPalindrome()
    {
        var sln = new Solution234();
        var testcase1 = LeetcodeHelper.CreateList([1, 2, 2, 1]);
        Assert.True(sln.IsPalindrome(testcase1));

        var testcase2 = LeetcodeHelper.CreateList([1, 2]);
        Assert.False(sln.IsPalindrome(testcase2));
    }
}