package gotest

// https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/

import (
	"testing"
)

func countKConstraintSubstrings(s string, k int) int {
	meetKConstraint := func(substr string) bool {
		zeroCount, oneCount := 0, 0
		for _, ch := range substr {
			if ch == '0' {
				zeroCount++
				if zeroCount > k && oneCount > k {
					return false
				}
			} else {
				oneCount++
				if oneCount > k && zeroCount > k {
					return false
				}
			}
		}
		// return zeroCount <= k && oneCount <= k
		return true
	}
	res := 0
	for subStrLen := 1; subStrLen <= len(s); subStrLen++ {
		for i := 0; i <= len(s)-subStrLen; i++ {
			if meetKConstraint(s[i : i+subStrLen]) {
				res++
			}
		}
	}
	return res
}

func TestCountKConstraintSubstrings(t *testing.T) {
	type args struct {
		s string
		k int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				s: "10101",
				k: 1,
			},
			output: 12,
		},
		{
			input: args{
				s: "1010101",
				k: 2,
			},
			output: 25,
		},
		{
			input: args{
				s: "11111",
				k: 1,
			},
			output: 15,
		},
	}
	for _, tc := range testcases {
		if got := countKConstraintSubstrings(tc.input.s, tc.input.k); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
