package gotest

// https://leetcode.cn/problems/search-a-2d-matrix-ii/description/
import (
	"testing"
)

func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	for i, j := 0, n-1; i < m && j >= 0; {
		if matrix[i][j] == target {
			return true
		} else if matrix[i][j] > target {
			j--
		} else {
			i++
		}
	}
	return false
}
func TestSearchMatrix(t *testing.T) {
	type args struct {
		matrix [][]int
		target int
	}
	testcases := []LeetcodeTestCase[args, bool]{
		{
			input: args{
				matrix: [][]int{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}},
				target: 5,
			},
			output: true,
		},
		{
			input: args{
				matrix: [][]int{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}},
				target: 20,
			},
			output: false,
		},
	}
	for _, tc := range testcases {
		got := searchMatrix(tc.input.matrix, tc.input.target)
		if got != tc.output {
			t.Errorf("searchMatrix(%v, %v) = %v, want %v", tc.input.matrix, tc.input.target, got, tc.output)
		}
	}
}
