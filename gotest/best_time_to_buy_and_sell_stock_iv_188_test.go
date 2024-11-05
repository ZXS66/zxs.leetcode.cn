package gotest

// https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/?envType=study-plan-v2&envId=top-interview-150
import (
	"math"
	"testing"
)

func maxProfitIV(k int, prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}

	k = min(k, n/2)
	buy := make([][]int, n)
	sell := make([][]int, n)
	for i := range buy {
		buy[i] = make([]int, k+1)
		sell[i] = make([]int, k+1)
	}
	buy[0][0] = -prices[0]
	for i := 1; i <= k; i++ {
		buy[0][i] = math.MinInt64 / 2
		sell[0][i] = math.MinInt64 / 2
	}

	for i := 1; i < n; i++ {
		buy[i][0] = max(buy[i-1][0], sell[i-1][0]-prices[i])
		for j := 1; j <= k; j++ {
			buy[i][j] = max(buy[i-1][j], sell[i-1][j]-prices[i])
			sell[i][j] = max(sell[i-1][j], buy[i-1][j-1]+prices[i])
		}
	}
	return maxInt(sell[n-1])
}
func maxInt(nums []int) int {
	res := nums[0]
	for _, v := range nums[1:] {
		if v > res {
			res = v
		}
	}
	return res
}
func TestMaxProfitIV(t *testing.T) {
	type args struct {
		k      int
		prices []int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				k:      2,
				prices: []int{2, 4, 1},
			},
			output: 2,
		},
		{
			input: args{
				k:      2,
				prices: []int{3, 2, 6, 5, 0, 3},
			},
			output: 7,
		},
	}
	for _, tc := range testcases {
		got := maxProfitIV(tc.input.k, tc.input.prices)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
