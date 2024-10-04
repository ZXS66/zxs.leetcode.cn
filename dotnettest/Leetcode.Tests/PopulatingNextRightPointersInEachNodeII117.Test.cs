namespace Leetcode.Tests;

public class PopulatingNextRightPointersInEachNodeII117Test
{
    [Fact]
    public void Connect()
    {
        var sln = new Solution117();
        var root = new BinaryNodeWithNextPointer(1)
        {
            left = new BinaryNodeWithNextPointer(2) { left = new BinaryNodeWithNextPointer(4), right = new BinaryNodeWithNextPointer(5) },
            right = new BinaryNodeWithNextPointer(3) { right = new BinaryNodeWithNextPointer(7) }
        };
        var result1 = sln.Connect(root);
        Assert.NotNull(result1);
    }
}
