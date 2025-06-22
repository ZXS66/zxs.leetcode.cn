namespace Leetcode.Tests;

public class IntersectionOfTwoLinkedLists160Test
{
    [Fact]
    public void GetIntersectionNode()
    {
        Tuple<int, int[], int[], int, int>[] testcases = [
            Tuple.Create(8, new int[] {4,1,8,4,5}, new int[] {5,6,1,8,4,5}, 2, 3),
            Tuple.Create(2, new int[] {1,9,1,2,4}, new int[] {3,2,4}, 3, 1),
            Tuple.Create(0, new int[] {2,6,4}, new int[] {1,5},3,2),
        ];
        var sln = new Solution160();
        foreach (var testcase in testcases)
        {
            var headA = LeetcodeHelper.CreateList(testcase.Item2);
            var headB = LeetcodeHelper.CreateList(testcase.Item3);
            if (testcase.Item1 != 0)
            {
                // reset intersection node
                int skipA = testcase.Item4;
                var dumpA = headA;
                while (skipA-- > 0)
                {
                    dumpA = dumpA.next;
                }
                int skipB = testcase.Item5;
                var dumpB = headB;
                while (skipB-- > 1)
                {
                    dumpB = dumpB.next;
                }
                dumpB.next = dumpA;
            }
            var output = sln.GetIntersectionNode(headA, headB);
            Assert.Equal(testcase.Item1, output != null ? output.val : 0);
        }
    }
}