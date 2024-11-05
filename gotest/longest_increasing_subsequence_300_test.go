package gotest

// https://leetcode.cn/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"slices"
	"testing"
)

func lengthOfLIS(nums []int) int {
	longest := make([]int, len(nums))
	longest[0] = 1
	for i := 1; i < len(nums); i++ {
		longest[i] = 1
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				longest[i] = max(longest[i], longest[j]+1)
			}
		}
	}
	return slices.Max(longest)
}
func TestLengthOfLIS(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{10, 9, 2, 5, 3, 7, 101, 18},
			output: 4,
		},
		{
			input:  []int{0, 1, 0, 3, 2, 3},
			output: 4,
		},
		{
			input:  []int{7, 7, 7, 7, 7, 7, 7},
			output: 1,
		},
	}
	for _, tc := range testcases {
		got := lengthOfLIS(tc.input)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
