namespace Leetcode.Tests;

public class DivideAStringIntoGroupsOfSizeK2138Test
{
    [Fact]
    public void GetIntersectionNode()
    {
        Tuple<string, string, int, char>[] testcases = [
            Tuple.Create("[\"abc\",\"def\",\"ghi\"]", "abcdefghi", 3, 'x'),
            Tuple.Create("[\"abc\",\"def\",\"ghi\",\"jxx\"]","abcdefghij", 3, 'x'),
        ];
        var sln = new Solution2138();
        foreach (var testcase in testcases)
        {
            var output = sln.DivideString(testcase.Item2, testcase.Item3, testcase.Item4);
            Assert.Equal(testcase.Item1, LeetcodeHelper.Array2String(output));
        }
    }
}