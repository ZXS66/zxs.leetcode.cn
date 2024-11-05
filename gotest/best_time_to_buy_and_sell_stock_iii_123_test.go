package gotest

// https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"math"
	"testing"
)

func maxProfit(prices []int) int {
	n := len(prices)
	if n < 2 {
		return 0
	}
	buy1, sell1, buy2, sell2 := math.MaxInt32, 0, math.MaxInt32, 0
	for _, price := range prices {
		buy1 = min(buy1, price)
		sell1 = max(sell1, price-buy1)
		buy2 = min(buy2, price-sell1)
		sell2 = max(sell2, price-buy2)
	}
	return sell2
}
func TestMaxProfit(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{3, 3, 5, 0, 0, 3, 1, 4},
			output: 6,
		},
		{
			input:  []int{1, 2, 3, 4, 5},
			output: 4,
		},
		{
			input:  []int{7, 6, 4, 3, 1},
			output: 0,
		},
		{
			input:  []int{1},
			output: 0,
		},
	}
	for _, tc := range testcases {
		got := maxProfit(tc.input)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
