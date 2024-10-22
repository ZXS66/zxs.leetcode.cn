package gotest

import (
	"strconv"
	"testing"
)

// https://leetcode.cn/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150

func addBinary(a string, b string) string {
	// 解法一：先转 int（十进制），再相加，再转 bit （二进制）
	// 错误：会溢出 math.MaxInt64
	// a_int, _ := strconv.ParseUint(a, 2, 64)
	// b_int, _ := strconv.ParseUint(b, 2, 64)
	// return strconv.FormatUint(a_int+b_int, 2)
	// 解法二：手动加
	ans := ""
	carry := 0
	lenA, lenB := len(a), len(b)
	n := max(lenA, lenB)

	for i := 0; i < n; i++ {
		if i < lenA {
			carry += int(a[lenA-i-1] - '0')
		}
		if i < lenB {
			carry += int(b[lenB-i-1] - '0')
		}
		ans = strconv.Itoa(carry%2) + ans
		carry /= 2
	}
	if carry > 0 {
		ans = "1" + ans
	}
	return ans
}

func TestAddBinary(t *testing.T) {
	type args struct {
		a string
		b string
	}
	testcases := []LeetcodeTestCase[args, string]{
		{
			input: args{
				a: "11",
				b: "1",
			},
			output: "100",
		},
		{
			input: args{
				a: "1010",
				b: "1011",
			},
			output: "10101",
		},
		{
			input: args{
				a: "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
				b: "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011",
			},
			output: "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000",
		},
	}
	for _, tc := range testcases {
		output := addBinary(tc.input.a, tc.input.b)
		if output != tc.output {
			t.Fatalf("output %v not equal to expected %v", output, tc.output)
		}
	}
}
