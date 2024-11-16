package gotest

// https://leetcode.cn/problems/single-element-in-a-sorted-array/description/
import "testing"

func singleNonDuplicate(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	left, right := 0, len(nums)-1
	ans := -1
	for left <= right {
		if left == right {
			ans = nums[left]
			break
		}
		mid := (left + right) / 2
		num := nums[mid]
		if num != nums[mid-1] && num != nums[mid+1] {
			ans = num
			break
		}
		if mid%2 == 1 {
			if num == nums[mid-1] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		} else {
			if num == nums[mid+1] {
				left = mid + 1
			} else {
				right = mid - 2
			}
		}
	}
	return ans
}
func TestSingleNonDuplicate(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{1, 1, 2, 3, 3, 4, 4, 8, 8},
			output: 2,
		},
		{
			input:  []int{3, 3, 7, 7, 10, 11, 11},
			output: 10,
		},
		{
			input:  []int{1, 1, 2},
			output: 2,
		},
	}
	for _, tc := range testcases {
		if got := singleNonDuplicate(tc.input); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
