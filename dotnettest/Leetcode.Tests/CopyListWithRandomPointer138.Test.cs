namespace Leetcode.Tests;

public class CopyListWithRandomPointer138Test
{
    [Fact]
    public void CopyRandomList()
    {
        Node node1 = new Node(7),
            node2 = new Node(13),
            node3 = new Node(11),
            node4 = new Node(10),
            node5 = new Node(1);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;
        // node1.random = null;
        node2.random = node1;
        node3.random = node5;
        node4.random = node3;
        node5.random = node1;
        var copiedNode = new Solution138().CopyRandomList(node1);
        Assert.NotNull(copiedNode);
    }
}



