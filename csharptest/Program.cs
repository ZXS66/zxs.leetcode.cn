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
    var copiedNode = new Solution138().CopyRandomList(node1);
    Console.WriteLine("--------------------------------------");
    printNode(copiedNode);
}

TestCase138();  // just run the test immediately
#endregion

#region test case 2414
void TestCase2414()
{
    var sln = new Solution2414();
    var result1 = sln.LongestContinuousSubstring("abacaba");
    var result2 = sln.LongestContinuousSubstring("abcde");
    if (result1 != 2 || result2 != 5)
    {
        throw new Exception("test case 2414 failed");
    }
    else
    {
        Console.WriteLine("test case 2414 passed");
    }
}
TestCase2414(); // just run the test immediately
#endregion

#region test case 92

void TestCase92()
{
    var sln = new Solution92();
    Func<int[], ListNode> createList = (arr) =>
    {
        ListNode head = new ListNode(arr[0]);
        ListNode cur = head;
        for (int i = 1; i < arr.Length; i++)
        {
            cur.next = new ListNode(arr[i]);
            cur = cur.next;
        }
        return head;
    };
    Func<ListNode, string> listNodeToString = (head) =>
    {
        List<int> values = new List<int>();
        while (head != null)
        {
            values.Add(head.val);
            head = head.next;
        }
        return $"[{string.Join(",", values)}]";
    };
    var result1 = sln.ReverseBetween(createList([1, 2, 3, 4, 5]), 2, 4);
    if (listNodeToString(result1) != "[1,4,3,2,5]")
    {
        throw new Exception("test case 92 failed");
    }
    var result2 = sln.ReverseBetween(createList([5]), 1, 1);
    if (listNodeToString(result2) != "[5]")
    {
        throw new Exception("test case 92 failed");
    }
    var result3 = sln.ReverseBetween(createList([5, 6, 7]), 1, 2);
    if (listNodeToString(result3) != "[6,5,7]")
    {
        throw new Exception("test case 92 failed");
    }
    var result4 = sln.ReverseBetween(createList([7, 8, 9]), 2, 3);
    if (listNodeToString(result4) != "[7,9,8]")
    {
        throw new Exception("test case 92 failed");
    }
    Console.WriteLine("test case 92 passed");
}

TestCase92();
#endregion


