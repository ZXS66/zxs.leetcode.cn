package gotest

// https://leetcode.cn/problems/edit-distance/description/?envType=study-plan-v2&envId=top-interview-150
import "testing"

func minDistance(word1 string, word2 string) int {
	n, m := len(word1), len(word2)
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, m)
		for j := range memo[i] {
			memo[i][j] = -1 // -1 表示还没有计算过
		}
	}
	var dfs func(int, int) int
	dfs = func(i, j int) (res int) {
		if i < 0 {
			return j + 1
		}
		if j < 0 {
			return i + 1
		}
		p := &memo[i][j]
		if *p != -1 { // 之前计算过
			return *p
		}
		defer func() { *p = res }() // 记忆化
		if word1[i] == word2[j] {
			return dfs(i-1, j-1)
		}
		return min(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1)) + 1
	}
	return dfs(n-1, m-1)
}

func Test_minDistance(t *testing.T) {
	type args struct {
		word1 string
		word2 string
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				word1: "horse",
				word2: "ros",
			},
			output: 3,
		},
		{
			input: args{
				word1: "intention",
				word2: "execution",
			},
			output: 5,
		},
		{
			input: args{
				word1: "a",
				word2: "b",
			},
			output: 1,
		},
	}
	for _, tc := range testcases {
		got := minDistance(tc.input.word1, tc.input.word2)
		if got != tc.output {
			t.Errorf("minDistance(%v,%v)=%v, want %v", tc.input.word1, tc.input.word2, got, tc.output)
		}
	}
}
