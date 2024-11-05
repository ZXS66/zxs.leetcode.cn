package gotest

// https://leetcode.cn/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150
import "testing"

func minPathSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	// 每次只能向下或者向右移动一步
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[0][0] = grid[0][0]
	for i := 1; i < m; i++ {
		dp[i][0] = dp[i-1][0] + grid[i][0]
	}
	for j := 1; j < n; j++ {
		dp[0][j] = dp[0][j-1] + grid[0][j]
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		}
	}
	return dp[m-1][n-1]
}
func TestMinPathSum(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]int, int]{
		{
			input:  [][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}},
			output: 7,
		},
		{
			input:  [][]int{{1, 2, 3}, {4, 5, 6}},
			output: 12,
		},
	}
	for _, tc := range testcases {
		got := minPathSum(tc.input)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
