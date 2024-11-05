package gotest

// https://leetcode.cn/problems/interleaving-string/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"testing"
)

func isInterleave(s1 string, s2 string, s3 string) bool {
	n, m, t := len(s1), len(s2), len(s3)
	if (n + m) != t {
		return false
	}
	f := make([][]bool, n+1)
	for i := 0; i <= n; i++ {
		f[i] = make([]bool, m+1)
	}
	f[0][0] = true
	for i := 0; i <= n; i++ {
		for j := 0; j <= m; j++ {
			p := i + j - 1
			if i > 0 {
				f[i][j] = f[i][j] || (f[i-1][j] && s1[i-1] == s3[p])
			}
			if j > 0 {
				f[i][j] = f[i][j] || (f[i][j-1] && s2[j-1] == s3[p])
			}
		}
	}
	return f[n][m]
}

func Test_isInterleave(t *testing.T) {
	type args struct {
		s1 string
		s2 string
		s3 string
	}
	tests := []LeetcodeTestCase[args, bool]{
		{
			input: args{
				s1: "aabcc",
				s2: "dbbca",
				s3: "aadbbcbcac",
			},
			output: true,
		},
		{
			input: args{
				s1: "aabcc",
				s2: "dbbca",
				s3: "aadbbbaccc",
			},
			output: false,
		},
		{
			input: args{
				s1: "",
				s2: "",
				s3: "",
			},
			output: true,
		},
		{
			input: args{
				s1: "abababababababababababababababababababababababababababababababababababababababababababababababababbb",
				s2: "babababababababababababababababababababababababababababababababababababababababababababababababaaaba",
				s3: "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb",
			},
			output: false,
		},
	}
	for _, tt := range tests {
		if got := isInterleave(tt.input.s1, tt.input.s2, tt.input.s3); got != tt.output {
			t.Errorf("isInterleave() = %v, want %v", got, tt.output)
		}
	}
}
