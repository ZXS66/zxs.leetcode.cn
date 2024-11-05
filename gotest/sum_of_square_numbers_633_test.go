package gotest

// https://leetcode.cn/problems/sum-of-square-numbers/
import (
	"math"
	"testing"
)

func judgeSquareSum(c int) bool {
	left, right := 0, int(math.Sqrt(float64(c)))
	for left <= right {
		sum := left*left + right*right
		if sum == c {
			return true
		} else if sum < c {
			left++
		} else {
			right--
		}
	}
	return left*left+right*right == c
}

func TestJudgeSquareSum(t *testing.T) {
	testcases := []LeetcodeTestCase[int, bool]{
		{
			input:  10,
			output: true,
		},
		{
			input:  5,
			output: true,
		},
		{
			input:  4,
			output: true,
		},
		{
			input:  3,
			output: false,
		},
		{
			input:  2,
			output: true,
		},
		{
			input:  1,
			output: true,
		},
		{
			input:  0,
			output: true,
		},
		{
			input:  2147483645,
			output: false,
		},
	}
	for _, tc := range testcases {
		if got := judgeSquareSum(tc.input); got != tc.output {
			t.Errorf("judgeSquareSum(%v)=%v, want %v", tc.input, got, tc.output)
		}
	}
}
