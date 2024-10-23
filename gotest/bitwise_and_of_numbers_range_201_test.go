package gotest

// https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"math/bits"
	"testing"
)

func rangeBitwiseAnd(left int, right int) int {
	// 以下解法超时
	// ret := left
	// for num := left + 1; num <= right; num++ {
	// 	ret &= num
	// }
	// return ret

	// 0 <= left <= right <= 231 - 1
	m := bits.Len(uint(left ^ right))
	return left &^ ((1 << m) - 1)
}

func TestRangeBitwiseAnd(t *testing.T) {
	type args struct {
		left  int
		right int
	}
	testCases := []LeetcodeTestCase[args, int]{
		{
			input:  args{left: 5, right: 7},
			output: 4,
		},
		{
			input:  args{left: 0, right: 0},
			output: 0,
		},
		{
			input:  args{left: 1, right: 2147483647},
			output: 0,
		},
	}
	for _, tc := range testCases {
		ret := rangeBitwiseAnd(tc.input.left, tc.input.right)
		if ret != tc.output {
			t.Errorf("rangeBitwiseAnd(%v, %v) = %v, want %v", tc.input.left, tc.input.right, ret, tc.output)
		}
	}
}
