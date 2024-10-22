package gotest

import (
	"strconv"
	"testing"
)

// https://leetcode.cn/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150

func reverseBits(num uint32) (ret uint32) {
	for i := 0; i < 32 && num > 0; i++ {
		ret |= num & 1 << (31 - i)
		num >>= 1
	}
	return
}

func TestReverseBits(t *testing.T) {
	testcases := []LeetcodeTestCase[string, uint32]{
		{
			input:  "00000010100101000001111010011100",
			output: 964176192,
		},
		{
			input:  "11111111111111111111111111111101",
			output: 3221225471,
		},
	}
	for _, testcase := range testcases {
		t.Run("TestReverseBits", func(t *testing.T) {
			num, _ := strconv.ParseUint(testcase.input, 2, 32)
			got := reverseBits(uint32(num))
			if got != testcase.output {
				t.Errorf("got %v, want %v", got, testcase.output)
			}
		})
	}
}
