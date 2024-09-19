// See https://aka.ms/new-console-template for more information
using System.Text;

Console.WriteLine("########################################");
Console.WriteLine("running test cases...");

#region test case 138
void TestCase138()
{
    Action<Node> printNode = (node) =>
    {
        Node cur = node;
        List<Node> nodeList = new List<Node>();
        while (cur != null)
        {
            nodeList.Add(cur);
            cur = cur.next;
        }
        StringBuilder sb = new StringBuilder();
        foreach (var item in nodeList)
        {
            if (item.random != null)
            {
                int idxOfRandom = nodeList.IndexOf(item.random);
                sb.Append($"[{item.val},{idxOfRandom}]");
            }
            else
            {
                sb.Append($"[{item.val},null]");
            }
        }
        Console.WriteLine("[" + string.Join(',', sb) + "]");
    };
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
    printNode(node1);
    var copiedNode = new Solution().CopyRandomList(node1);
    Console.WriteLine("--------------------------------------");
    printNode(copiedNode);
}
#endregion

TestCase138();

