package gotest

// https://leetcode.cn/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"testing"
)

func wordBreak(s string, wordDict []string) bool {
	maxLen := 0
	words := make(map[string]bool, len(wordDict))
	for _, w := range wordDict {
		words[w] = true
		maxLen = max(maxLen, len(w))
	}

	n := len(s)
	memo := make([]int8, n+1)
	for i := range memo {
		memo[i] = -1 // -1 表示没有计算过
	}
	var dfs func(int) int8
	dfs = func(i int) (res int8) {
		if i == 0 { // 成功拆分！
			return 1
		}
		p := &memo[i]
		if *p != -1 { // 之前计算过
			return *p
		}
		defer func() { *p = res }() // 记忆化
		for j := i - 1; j >= max(i-maxLen, 0); j-- {
			if words[s[j:i]] && dfs(j) == 1 {
				return 1
			}
		}
		return 0
	}
	return dfs(n) == 1
}

func Test_wordBreak(t *testing.T) {
	type args struct {
		s        string
		wordDict []string
	}
	testcases := []LeetcodeTestCase[args, bool]{
		{
			input: args{
				s:        "leetcode",
				wordDict: []string{"leet", "code"},
			},
			output: true,
		},
		{
			input: args{
				s:        "applepenapple",
				wordDict: []string{"apple", "pen"},
			},
			output: true,
		},
		{
			input: args{
				s:        "catsandog",
				wordDict: []string{"cats", "dog", "sand", "and", "cat"},
			},
			output: false,
		},
	}
	for _, tc := range testcases {
		if got := wordBreak(tc.input.s, tc.input.wordDict); got != tc.output {
			t.Errorf("wordBreak(%v, %v) = %v, want %v", tc.input.s, tc.input.wordDict, got, tc.output)
		}
	}
}
