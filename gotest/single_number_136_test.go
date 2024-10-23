package gotest

// https://leetcode.cn/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150
// 要求：你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

import (
	"testing"
)

func singleNumber(nums []int) (ret int) {
	// counter := make(map[int]bool)
	// for _, num := range nums {
	// 	_, ok := counter[num]
	// 	if ok {
	// 		// existing number
	// 		delete(counter, num)
	// 	} else {
	// 		counter[num] = true
	// 	}
	// }
	// // return the only one number
	// for k := range counter {
	// 	ret = k
	// 	break // return
	// }
	// return
	for _, num := range nums {
		ret ^= num
	}
	return
}

func TestSingleNumber(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{2, 2, 1},
			output: 1,
		},
		{
			input:  []int{4, 1, 2, 1, 2},
			output: 4,
		},
		{
			input:  []int{1},
			output: 1,
		},
	}
	t.Run("singleNumber", func(t *testing.T) {
		for _, tc := range testcases {
			got := singleNumber(tc.input)
			if got != tc.output {
				t.Errorf("input: %v, expected: %v, got: %v", tc.input, tc.output, got)
			}
		}
	})
}
