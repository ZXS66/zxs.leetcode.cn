package gotest

import (
	"fmt"
	"strings"
	"testing"
)

// https://leetcode.cn/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150

func hammingWeight(n int) int {
	n_binary := fmt.Sprintf("%b", n)
	return strings.Count(n_binary, "1")
}

func TestHammingWeight(t *testing.T) {
	testcases := []LeetcodeTestCase[int, int]{
		{
			input:  11,
			output: 3,
		},
		{
			input:  128,
			output: 1,
		},
		{
			input:  2147483645,
			output: 30,
		},
	}
	t.Run("TestHammingWeight", func(t *testing.T) {
		for _, testcase := range testcases {
			output := hammingWeight(testcase.input)
			if output != testcase.output {
				t.Errorf("hammingWeight(%v) = %v, want %v", testcase.input, output, testcase.output)
			}
		}
	})
}
