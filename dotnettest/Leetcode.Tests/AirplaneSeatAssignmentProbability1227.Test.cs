namespace Leetcode.Tests;

public class AirplaneSeatAssignmentProbability1227Test
{
    [Fact]
    public void NthPersonGetsNthSeat()
    {
        var solution = new Solution1227();
        Assert.Equal(1, solution.NthPersonGetsNthSeat(1));
        Assert.Equal(0.5, solution.NthPersonGetsNthSeat(2));
    }
}

