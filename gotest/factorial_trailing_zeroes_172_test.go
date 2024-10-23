package gotest

// https://leetcode.cn/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"testing"
)

func trailingZeroes(n int) int {
	ans := 0
	for n > 0 {
		n = int(n / 5)
		ans += n
	}
	return ans
}

func Test_trailingZeroes(t *testing.T) {
	testcases := []LeetcodeTestCase[int, int]{
		{
			input:  3,
			output: 0,
		},
		{
			input:  5,
			output: 1,
		},
		{
			input:  0,
			output: 0,
		},
	}
	for _, tc := range testcases {
		if ans := trailingZeroes(tc.input); ans != tc.output {
			t.Errorf("trailingZeroes(%v) = %v, want %v", tc.input, ans, tc.output)
		}
	}
}
