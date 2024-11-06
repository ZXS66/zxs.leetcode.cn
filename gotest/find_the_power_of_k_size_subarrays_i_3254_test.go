package gotest

// https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/description/
import (
	"reflect"
	"testing"
)

func resultsArray(nums []int, k int) []int {
	n := len(nums)
	if n == 1 || k == 1 {
		return nums
	}
	result := make([]int, n-k+1)
	prevNum := nums[0]
	idxOfFirstK := 0
	for i := 1; i < n; i++ {
		if nums[i] != prevNum+1 {
			// 非 连续 且 上升 的元素
			idxOfFirstK = i
		}
		prevNum = nums[i]
		if i < k-1 {
			continue
		}
		if i-k+1 >= idxOfFirstK {
			// 依次 连续 且 上升 的
			result[i-k+1] = nums[i]
		} else {
			result[i-k+1] = -1
		}
	}
	return result
}
func TestResultsArray(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	testcases := []LeetcodeTestCase[args, []int]{
		{
			input: args{
				nums: []int{1, 2, 3, 4, 3, 2, 5},
				k:    3,
			},
			output: []int{3, 4, -1, -1, -1},
		},
		{
			input: args{
				nums: []int{2, 2, 2, 2, 2},
				k:    4,
			},
			output: []int{-1, -1},
		},
		{
			input: args{
				nums: []int{3, 2, 3, 2, 3, 2},
				k:    2,
			},
			output: []int{-1, 3, -1, 3, -1},
		},
		{
			input: args{
				nums: []int{1, 4},
				k:    1,
			},
			output: []int{1, 4},
		},
		{
			input: args{
				nums: []int{1, 3, 4},
				k:    2,
			},
			output: []int{-1, 4},
		},
	}
	for _, tc := range testcases {
		got := resultsArray(tc.input.nums, tc.input.k)
		if !reflect.DeepEqual(got, tc.output) {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
