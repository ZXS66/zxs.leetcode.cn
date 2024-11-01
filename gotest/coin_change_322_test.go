package gotest

// https://leetcode.cn/problems/coin-change/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"slices"
	"testing"
)

func coinChange(coins []int, amount int) int {
	slices.Sort(coins)
	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = -1
		for _, coin := range coins {
			if coin > i {
				break
			}
			if dp[i-coin] == -1 {
				continue
			}
			if dp[i] == -1 || dp[i] > dp[i-coin]+1 {
				dp[i] = dp[i-coin] + 1
			}
		}
	}
	return dp[amount]
}
func TestCoinChange(t *testing.T) {
	type args struct {
		coins  []int
		amount int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				coins:  []int{1, 2, 5},
				amount: 11,
			},
			output: 3,
		},
		{
			input: args{
				coins:  []int{2},
				amount: 3,
			},
			output: -1,
		},
		{
			input: args{
				coins:  []int{1},
				amount: 0,
			},
			output: 0,
		},
		{
			input: args{
				coins:  []int{186, 419, 83, 408},
				amount: 6249,
			},
			output: 20,
		},
	}
	for _, tc := range testcases {
		if got := coinChange(tc.input.coins, tc.input.amount); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
