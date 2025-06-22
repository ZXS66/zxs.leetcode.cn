/// <summary>handy helper functions</summary>
public static class LeetcodeHelper
{
    /// <summary>create <see cref="ListNode"/> via list of integer number</summary>
    /// <param name="arr"></param>
    /// <returns></returns>
    public static ListNode CreateList(int[] arr)
    {
        ListNode head = new ListNode(arr[0]);
        ListNode cur = head;
        for (int i = 1; i < arr.Length; i++)
        {
            cur.next = new ListNode(arr[i]);
            cur = cur.next;
        }
        return head;
    }
    /// <summary>parse <see cref="ListNode"/> as string</summary>
    /// <param name="head"></param>
    /// <returns></returns>
    public static string ListNodeToString(ListNode head)
    {
        List<int> values = new List<int>();
        while (head != null)
        {
            values.Add(head.val);
            head = head.next;
        }
        return $"[{string.Join(",", values)}]";
    }
    /// <summary>create <seealso cref="TreeNode"/> via list of integer number</summary>
    /// <param name="arr"></param>
    /// <returns></returns>
    public static TreeNode CreateTree(int?[] arr)
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
    }
    /// <summary>parse <see cref="TreeNode"/> as string</summary>
    /// <param name="root"></param>
    /// <returns></returns>
    public static string TreeToString(TreeNode root)
    {
        if (root == null)
        {
            return "null";
        }
        // return $"{root.val},{treeToString(root.left)},{treeToString(root.right)}";
        List<int?> nodes = new List<int?>();
        Queue<TreeNode?> queue = new Queue<TreeNode?>();
        queue.Enqueue(root);
        int depth = 0, count = 0;
        bool hasLeafNodesOfCurrentDepth = false;
        while (true)
        {
            TreeNode? cur = queue.Dequeue();
            nodes.Add(cur?.val);
            queue.Enqueue(cur?.left);
            queue.Enqueue(cur?.right);
            hasLeafNodesOfCurrentDepth = hasLeafNodesOfCurrentDepth || cur?.left != null || cur?.right != null;
            count++;
            if (count == Math.Pow(2, depth))
            {
                if (!hasLeafNodesOfCurrentDepth)
                {
                    break;
                }
                hasLeafNodesOfCurrentDepth = false;
                depth++;
                count = 0;
            }
        }
        return String.Join(",", nodes.Select(n => n.HasValue ? n.Value.ToString() : "null"));
    }

    public static string Array2String<T>(T[] arr)
    {
        if (arr == null || arr.Length == 0)
        {
            return String.Empty;
        }
        return System.Text.Json.JsonSerializer.Serialize(arr);
    }
}