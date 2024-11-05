package gotest

// https://leetcode.cn/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150
import "testing"

func longestPalindrome(s string) string {
	dp := make([][]bool, len(s)) // dp[i][j] 表示 s[i:j] 是否为回文串
	for i := range dp {
		dp[i] = make([]bool, len(s))
	}
	for i := len(s) - 1; i >= 0; i-- {
		dp[i][i] = true
		for j := i + 1; j < len(s); j++ {
			dp[i][j] = (s[i] == s[j]) && (j-i <= 2 || dp[i+1][j-1])
		}
	}
	var res string
	for i := range s {
		for j := i; j < len(s); j++ {
			if dp[i][j] && j-i+1 > len(res) {
				res = s[i : j+1]
			}
		}
	}
	return res
}
func TestLongestPalindrome(t *testing.T) {
	testcases := []LeetcodeTestCase[string, string]{
		{
			input:  "babad",
			output: "bab",
		},
		{
			input:  "cbbd",
			output: "bb",
		},
	}
	for _, tc := range testcases {
		if res := longestPalindrome(tc.input); res != tc.output {
			t.Errorf("longestPalindrome(%v) = %v, want %v", tc.input, res, tc.output)
		}
	}
}
