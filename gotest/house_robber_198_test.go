package gotest

// https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"testing"
)

func rob(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	} else if n == 2 {
		return max(nums[0], nums[1])
	}
	wallet := make([]int, n)
	wallet[0] = nums[0]
	wallet[1] = max(nums[0], nums[1])
	for i := 2; i < n; i++ {
		wallet[i] = max(wallet[i-1], wallet[i-2]+nums[i])
	}
	return wallet[n-1]
}

func Test_rob(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{1, 2, 3, 1},
			output: 4,
		},
		{
			input:  []int{2, 7, 9, 3, 1},
			output: 12,
		},
		{
			input:  []int{2, 1, 1, 2},
			output: 4,
		},
	}
	for _, tc := range testcases {
		if got := rob(tc.input); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
