package gotest

// https://leetcode.cn/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
// 结果只保留 整数部分 ，小数部分将被 舍去
// 不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5

import (
	"math"
	"testing"
)

func mySqrt(x int) int {
	// 0 <= x <= 2^31 - 1
	if x == 0 || x == 1 {
		return x
	} else if x == 2 || x == 3 {
		return 1
	}
	// 二分查找
	left := 1
	right := x / 2 // 最大值不超过x/2
	for left <= right {
		mid := int(math.Ceil((float64(left) + float64(right)) / 2))
		square := mid * mid
		if square == x {
			return mid
		} else if square < x {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	if left*left > x {
		return left - 1
	} else {
		return left
	}
}

func TestMySqrt(t *testing.T) {
	testcases := []LeetcodeTestCase[int, int]{
		{
			input:  4,
			output: 2,
		},
		{
			input:  8,
			output: 2,
		},
		{
			input:  1,
			output: 1,
		},
		{
			input:  17,
			output: 4,
		},
		{
			input:  2,
			output: 1,
		},
		{
			input:  9,
			output: 3,
		},
	}
	for _, tc := range testcases {
		if res := mySqrt(tc.input); res != tc.output {
			t.Errorf("mySqrt(%d) = %d, want %d", tc.input, res, tc.output)
		}
	}
}
