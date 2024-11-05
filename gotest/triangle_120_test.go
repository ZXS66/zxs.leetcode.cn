package gotest

// https://leetcode.cn/problems/triangle/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"slices"
	"testing"
)

func minimumTotal(triangle [][]int) int {
	if len(triangle) == 0 {
		return triangle[0][0]
	}
	path := make([]int, len(triangle))
	path[0] = triangle[0][0]
	for i := 1; i < len(triangle); i++ {
		path[i] = path[i-1] + triangle[i][i]
		for j := i - 1; j > 0; j-- {
			path[j] = min(path[j-1], path[j]) + triangle[i][j]
		}
		path[0] += triangle[i][0]
	}
	return slices.Min(path)
}
func TestMinimumTotal(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]int, int]{
		{
			input: [][]int{
				{2},
				{3, 4},
				{6, 5, 7},
				{4, 1, 8, 3},
			},
			output: 11,
		},
		{
			input: [][]int{
				{-10},
			},
			output: -10,
		},
	}
	for _, tc := range testcases {
		got := minimumTotal(tc.input)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
