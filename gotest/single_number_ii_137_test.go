package gotest

// https://leetcode.cn/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150
// 要求：你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

import (
	"testing"
)

func singleNumberII(nums []int) int {
	// counter := make(map[int]int)
	// for _, num := range nums {
	// 	cnt, ok := counter[num]
	// 	if ok {
	// 		// existing number
	// 		if cnt == 2 {
	// 			delete(counter, num)
	// 			continue
	// 		}
	// 		counter[num]++
	// 	} else {
	// 		counter[num] = 1
	// 	}
	// }
	// // return the only one number
	// ret := 0
	// for k := range counter {
	// 	ret = k
	// 	break // return
	// }
	// return ret
	a, b := 0, 0
	for _, num := range nums {
		b = (b ^ num) &^ a
		a = (a ^ num) &^ b
	}
	return b
	// 链接：https://leetcode.cn/problems/single-number-ii/solutions/746993/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
}

func TestSingleNumberII(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{2, 2, 3, 2},
			output: 3,
		},
		{
			input:  []int{0, 1, 0, 1, 0, 1, 99},
			output: 99,
		},
	}
	t.Run("singleNumberII", func(t *testing.T) {
		for _, tc := range testcases {
			got := singleNumberII(tc.input)
			if got != tc.output {
				t.Errorf("input: %v, expected: %v, got: %v", tc.input, tc.output, got)
			}
		}
	})
}
