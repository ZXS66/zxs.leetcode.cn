namespace Leetcode.Tests;

public class SumOfKMirrorNumbers2081Test
{
    [Fact]
    public void KMirror()
    {
        Tuple<long, int, int>[] testcases = [
            Tuple.Create(25L, 2, 5),
            Tuple.Create(499L, 3, 7),
            Tuple.Create(20379000L, 7, 17),
        ];
        var sln = new Solution2081();
        foreach (var testcase in testcases)
        {
            var output = sln.KMirror(testcase.Item2, testcase.Item3);
            Assert.Equal(output, testcase.Item1);
        }
    }
}
