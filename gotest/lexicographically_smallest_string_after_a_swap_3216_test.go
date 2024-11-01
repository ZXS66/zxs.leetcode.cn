package gotest

// https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/description/
import "testing"

func getSmallestString(s string) string {
	for i := 0; i < len(s)-1; i++ {
		a, b := s[i], s[i+1]
		if a == b {
			// 相同数字，交换无意义（数值不变）
			continue
		}
		if a%2 != b%2 {
			// 具有不同奇偶性，不符合题目要求
			continue
		}
		if a < b {
			// 交换后数值变大，还不如不交换
			continue
		}
		return s[:i] + string(b) + string(a) + s[i+2:]
	}
	return s
}

func TestGetSmallestString(t *testing.T) {
	testcases := []LeetcodeTestCase[string, string]{
		{
			input:  "45320",
			output: "43520",
		},
		{
			input:  "001",
			output: "001",
		},
	}
	for _, tc := range testcases {
		if got := getSmallestString(tc.input); got != tc.output {
			t.Errorf("getSmallestString(%v) = %v, want %v", tc.input, got, tc.output)
		}
	}
}
