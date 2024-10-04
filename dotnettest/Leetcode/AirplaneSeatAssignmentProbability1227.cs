// https://leetcode.cn/problems/airplane-seat-assignment-probability/

public class Solution1227 {
    public double NthPersonGetsNthSeat(int n) {
        return n == 1 ? 1 : 0.5;
    }
}