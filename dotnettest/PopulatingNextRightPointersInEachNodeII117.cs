// https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

using System.Collections;
using System.ComponentModel.Design.Serialization;
using System.Xml.Serialization;
using Node = BinaryNodeWithNextPointer;

public class Solution117
{
    public BinaryNodeWithNextPointer Connect(BinaryNodeWithNextPointer root)
    {
        #region approach that out of memory
        // if (root == null)
        // {
        //     return null;
        // }
        // Queue<Node?> queue = new Queue<Node?>();
        // queue.Enqueue(root);
        // int depth = 0, count = 0;
        // bool hasLeafNodesOfCurrentDepth = false;
        // Node? prev = null;
        // while (true)
        // {
        //     Node? node = queue.Dequeue();
        //     queue.Enqueue(node?.left);
        //     queue.Enqueue(node?.right);
        //     hasLeafNodesOfCurrentDepth = hasLeafNodesOfCurrentDepth || node?.left != null || node?.right != null;
        //     count++;
        //     if (prev != null && node != null)
        //     {
        //         prev.next = node;
        //     }
        //     if (node != null)
        //     {
        //         prev = node;
        //     }
        //     if (count == Math.Pow(2, depth))
        //     {
        //         if (!hasLeafNodesOfCurrentDepth)
        //         {
        //             break;
        //         }
        //         hasLeafNodesOfCurrentDepth = false;
        //         depth++;
        //         count = 0;
        //         if (node != null)
        //         {
        //             node.next = null;
        //         }
        //         prev = null;
        //     }
        // }
        // return root;
        #endregion

        if (root == null)
        {
            return null;
        }
        Queue<BinaryNodeWithNextPointer> theQueue = new Queue<BinaryNodeWithNextPointer>();
        theQueue.Enqueue(root);
        while (theQueue.Count > 0)
        {
            int size = theQueue.Count;
            BinaryNodeWithNextPointer prev = null;
            for (int i = 1; i <= size; ++i)
            {
                BinaryNodeWithNextPointer node = theQueue.Dequeue();
                if (node.left != null)
                {
                    theQueue.Enqueue(node.left);
                }
                if (node.right != null)
                {
                    theQueue.Enqueue(node.right);
                }
                if (prev != null)
                {
                    prev.next = node;
                }
                prev = node;
            }
        }
        return root;
    }
}