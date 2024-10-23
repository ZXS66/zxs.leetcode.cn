package gotest

import (
	"testing"
)

// https://leetcode.cn/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150

func plusOne(digits []int) []int {
	surplus := 1
	for i := len(digits) - 1; i >= 0; i-- {
		digits[i] += surplus
		if digits[i] == 10 {
			digits[i] = 0
			surplus = 1
		} else {
			surplus = 0
			break
		}
	}
	if surplus == 1 {
		digits = append([]int{1}, digits...)
	}
	return digits
}

func TestPlusOne(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, []int]{
		{
			input:  []int{1, 2, 3},
			output: []int{1, 2, 4},
		},
		{
			input:  []int{4, 3, 2, 1},
			output: []int{4, 3, 2, 2},
		},
		{
			input:  []int{9},
			output: []int{1, 0},
		},
		{
			input:  []int{0},
			output: []int{1},
		},
		{
			input:  []int{9, 9},
			output: []int{1, 0, 0},
		},
	}
	for _, tc := range testcases {
		actual := plusOne(tc.input)
		if len(actual) != len(tc.output) {
			t.Errorf("Expected %v, got %v", tc.output, actual)
		} else {
			for i := 0; i < len(actual); i++ {
				if actual[i] != tc.output[i] {
					t.Errorf("Expected %v, got %v", tc.output, actual)
				}
			}
		}
	}
}
