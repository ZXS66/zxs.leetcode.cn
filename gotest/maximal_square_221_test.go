package gotest

// https://leetcode.cn/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150
import "testing"

func maximalSquare(matrix [][]byte) int {
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m) // dp[i][j] 表示以 matrix[i][j] 为右下角的正方形的边长
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '0' {
				dp[i][j] = 0
			} else {
				if i == 0 || j == 0 {
					dp[i][j] = 1
				} else {
					dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
				}
			}
		}
	}
	ans := 0
	for _, row := range dp {
		for _, v := range row {
			ans = max(ans, v)
		}
	}
	return ans * ans
}
func TestMaximalSquare(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]byte, int]{
		{
			input: [][]byte{
				{'1', '0', '1', '0', '0'},
				{'1', '0', '1', '1', '1'},
				{'1', '1', '1', '1', '1'},
				{'1', '0', '0', '1', '0'},
			},
			output: 4,
		},
		{
			input: [][]byte{
				{'0', '1'},
				{'1', '0'},
			},
			output: 1,
		},
		{
			input: [][]byte{
				{'0'},
			},
			output: 0,
		},
	}
	for _, tc := range testcases {
		got := maximalSquare(tc.input)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
