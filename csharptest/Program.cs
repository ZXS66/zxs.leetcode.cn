// See https://aka.ms/new-console-template for more information
using System.Text;

Console.WriteLine("########################################");
Console.WriteLine("running test cases...");

#region handy functions

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

Func<int?[], TreeNode> createTree = (arr) =>
{
    if (arr == null || arr.Length == 0)
    {
        return null;
    }
    int n = arr.Length;
    IDictionary<int, TreeNode> dict = new Dictionary<int, TreeNode>();
    for (int i = 0; i < n; i++)
    {
        if (arr[i].HasValue)
        {
            dict[i] = new TreeNode(arr[i].Value);
        }
    }
    // the second for loop can be optimized
    for (int i = 0; i < n; i++)
    {
        if (arr[i].HasValue)
        {
            int left = 2 * i + 1, right = 2 * i + 2;
            if (left < n && arr[left].HasValue)
            {
                dict[i].left = dict[left];
            }
            if (right < n && arr[right].HasValue)
            {
                dict[i].right = dict[right];
            }
        }
    }
    return dict[0];
};
#endregion



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

//TestCase138();  // just run the test immediately
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
// TestCase2414(); // just run the test immediately
#endregion

#region test case 92

void TestCase92()
{
    var sln = new Solution92();
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

//TestCase92();
#endregion


#region test case 25

void TestCase25()
{
    var sln = new Solution25();
    var result1 = sln.ReverseKGroup(createList([1, 2, 3, 4, 5]), 2);
    if (listNodeToString(result1) != "[2,1,4,3,5]")
    {
        throw new Exception("test case 25 failed");
    }
    var result2 = sln.ReverseKGroup(createList([1, 2, 3, 4, 5]), 3);
    if (listNodeToString(result2) != "[3,2,1,4,5]")
    {
        throw new Exception("test case 25 failed");
    }
    var result3 = sln.ReverseKGroup(createList([1, 2]), 2);
    if (listNodeToString(result3) != "[2,1]")
    {
        throw new Exception("test case 25 failed");
    }
    Console.WriteLine("test case 25 passed");
}

// TestCase25();
#endregion

#region test case 19
void TestCase19()
{
    var sln = new Solution19();
    var result1 = sln.RemoveNthFromEnd(createList([1, 2, 3, 4, 5]), 2);
    if (listNodeToString(result1) != "[1,2,3,5]")
    {
        throw new Exception("test case 19 failed");
    }
    var result2 = sln.RemoveNthFromEnd(createList([1]), 1);
    if (listNodeToString(result2) != "[]")
    {
        throw new Exception("test case 19 failed");
    }
    var result3 = sln.RemoveNthFromEnd(createList([1, 2]), 1);
    if (listNodeToString(result3) != "[1]")
    {
        throw new Exception("test case 19 failed");
    }
    var result4 = sln.RemoveNthFromEnd(createList([1, 2]), 2);
    if (listNodeToString(result4) != "[2]")
    {
        throw new Exception("test case 19 failed");
    }
    Console.WriteLine("test case 19 passed");
}

// TestCase19();

#endregion

#region test case 82

void TestCase82()
{
    var sln = new Solution82();
    var result1 = sln.DeleteDuplicates(createList([1, 2, 3, 3, 4, 4, 5]));
    if (listNodeToString(result1) != "[1,2,5]")
    {
        throw new Exception("test case 82 failed");
    }
    var result2 = sln.DeleteDuplicates(createList([1, 1, 1, 2, 3]));
    if (listNodeToString(result2) != "[2,3]")
    {
        throw new Exception("test case 82 failed");
    }
    var result3 = sln.DeleteDuplicates(createList([1, 1]));
    if (listNodeToString(result3) != "[]")
    {
        throw new Exception("test case 82 failed");
    }
    Console.WriteLine("test case 82 passed");
}
// TestCase82();
#endregion


#region test case 997

void TestCase997()
{
    var sln = new Solution997();
    var result1 = sln.FindJudge(2, [[1, 2]]);
    if (result1 != 2)
    {
        throw new Exception("test case 997 failed");
    }
    var result2 = sln.FindJudge(3, [[1, 3], [2, 3]]);
    if (result2 != 3)
    {
        throw new Exception("test case 997 failed");
    }
    var result3 = sln.FindJudge(3, [[1, 3], [2, 3], [3, 1]]);
    if (result3 != -1)
    {
        throw new Exception("test case 997 failed");
    }
    var result4 = sln.FindJudge(1, []);
    if (result4 != 1)
    {
        throw new Exception("test case 997 failed");
    }
    Console.WriteLine("test case 997 passed");
}

// TestCase997();

#endregion



#region  test case 61

void TestCase61()
{
    var sln = new Solution61();
    var result1 = sln.RotateRight(createList([1, 2, 3, 4, 5]), 2);
    if (listNodeToString(result1) != "[4,5,1,2,3]")
    {
        throw new Exception("test case 61 failed");
    }
    var result2 = sln.RotateRight(createList([0, 1, 2]), 4);
    if (listNodeToString(result2) != "[2,0,1]")
    {
        throw new Exception("test case 61 failed");
    }
    Console.WriteLine("test case 61 passed");
}

// TestCase61();

#endregion


#region test case 86

void TestCase86()
{
    var sln = new Solution86();
    var result1 = sln.Partition(createList([1, 4, 3, 2, 5, 2]), 3);
    if (listNodeToString(result1) != "[1,2,2,4,3,5]")
    {
        throw new Exception("test case 86 failed");
    }
    var result2 = sln.Partition(createList([2, 1]), 2);
    if (listNodeToString(result2) != "[1,2]")
    {
        throw new Exception("test case 86 failed");
    }
    Console.WriteLine("test case 86 passed");
}
// TestCase86();
#endregion


#region test case 146
void TestCase146()
{
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.Put(1, 1); // 缓存是 {1=1}
    lRUCache.Put(2, 2); // 缓存是 {1=1, 2=2}
    var result1 = lRUCache.Get(1);    // 返回 1
    if (result1 != 1)
    {
        throw new Exception("test case 146 failed");
    }
    lRUCache.Put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    var result2 = lRUCache.Get(2);    // 返回 -1 (未找到)
    if (result2 != -1)
    {
        throw new Exception("test case 146 failed");
    }
    lRUCache.Put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    var result3 = lRUCache.Get(1);    // 返回 -1 (未找到)
    var result4 = lRUCache.Get(3);    // 返回 3
    var result5 = lRUCache.Get(4);    // 返回 4
    if (result3 != -1 || result4 != 3 || result5 != 4)
    {
        throw new Exception("test case 146 failed");
    }
    LRUCache lRUCache2 = new LRUCache(2);
    lRUCache2.Put(2, 1);
    lRUCache2.Put(1, 1);
    lRUCache2.Put(2, 3);
    lRUCache2.Put(4, 1);
    var result6 = lRUCache2.Get(1);
    var result7 = lRUCache2.Get(2);
    if (result6 != -1 || result7 != 3)
    {
        throw new Exception("test case 146 failed");
    }

    Console.WriteLine("test case 146 passed");
}
// TestCase146();
#endregion

#region test case 104
void TestCase104()
{
    var sln = new Solution104();
    var result1 = sln.MaxDepth(createTree([3, 9, 20, null, null, 15, 7]));
    if (result1 != 3)
    {
        throw new Exception("test case 104 failed");
    }
    var result2 = sln.MaxDepth(createTree([1, null, 2]));
    if (result2 != 2)
    {
        throw new Exception("test case 104 failed");
    }
    Console.WriteLine("test case 104 passed");
}
TestCase104();
#endregion

