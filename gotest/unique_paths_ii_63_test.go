package gotest

// https://leetcode.cn/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=top-interview-150
import "testing"

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m, n := len(obstacleGrid), len(obstacleGrid[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[i][j] = 0
			} else if i == 0 && j == 0 {
				dp[i][j] = 1
			} else if i == 0 {
				dp[i][j] = dp[i][j-1]
			}
		}
	}
	for i := 1; i < m; i++ {
		for j := 0; j < n; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[i][j] = 0
			} else if j == 0 {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}
	return dp[m-1][n-1]
}

func TestUniquePathsWithObstacles(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]int, int]{
		{
			input: [][]int{
				{0, 0, 0},
				{0, 1, 0},
				{0, 0, 0},
			},
			output: 2,
		},
		{
			input: [][]int{
				{0, 1},
				{0, 0},
			},
			output: 1,
		},
	}
	for _, tc := range testcases {
		got := uniquePathsWithObstacles(tc.input)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
