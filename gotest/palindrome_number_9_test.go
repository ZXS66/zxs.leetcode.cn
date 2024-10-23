package gotest

// https://leetcode.cn/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"testing"
)

func isPalindrome(x int) bool {
	// x_str := fmt.Sprintf("%d", x)
	// for i, j := 0, len(x_str)-1; i < j; i, j = i+1, j-1 {
	// 	if x_str[i] != x_str[j] {
	// 		return false
	// 	}
	// }
	// return true
	// 进阶：你能不将整数转为字符串来解决这个问题吗？
	if x < 0 {
		// 复数
		return false
	} else if x < 10 {
		// 个位数 [0,9]
		return true
	} else if x%10 == 0 {
		// 个位数为0的数字
		return false
	}
	bits := make([]int, 0)
	length := 0
	for x > 0 {
		a := x % 10
		bits = append(bits, a)
		x /= 10
		length++
	}
	for i, j := 0, length-1; i < j; i, j = i+1, j-1 {
		if bits[i] != bits[j] {
			return false
		}
	}
	return true
}

func TestIsPalindrome(t *testing.T) {
	testcases := []LeetcodeTestCase[int, bool]{
		{
			input:  123,
			output: false,
		},
		{
			input:  -123,
			output: false,
		},
		{
			input:  121,
			output: true,
		},
		{
			input:  0,
			output: true,
		},
		{
			input:  10,
			output: false,
		},
	}
	for _, tc := range testcases {
		if res := isPalindrome(tc.input); res != tc.output {
			t.Errorf("isPalindrome(%v) = %v, want %v", tc.input, res, tc.output)
		}
	}
}
