package gotest

// https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/
import "testing"

func minFlips(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ans := 0

	for i, row := range grid[:m/2] {
		row2 := grid[m-1-i]
		for j, x := range row[:n/2] {
			cnt1 := x + row[n-1-j] + row2[j] + row2[n-1-j]
			ans += min(cnt1, 4-cnt1) // 全为 1 或全为 0
		}
	}

	if m%2 > 0 && n%2 > 0 {
		// 正中间的数必须是 0
		ans += grid[m/2][n/2]
	}

	diff, cnt1 := 0, 0
	if m%2 > 0 {
		// 统计正中间这一排
		row := grid[m/2]
		for j, x := range row[:n/2] {
			if x != row[n-1-j] {
				diff++
			} else {
				cnt1 += x * 2
			}
		}
	}
	if n%2 > 0 {
		// 统计正中间这一列
		for i, row := range grid[:m/2] {
			if row[n/2] != grid[m-1-i][n/2] {
				diff++
			} else {
				cnt1 += row[n/2] * 2
			}
		}
	}

	if diff > 0 {
		ans += diff
	} else {
		ans += cnt1 % 4
	}
	return ans
}

func TestMinFlips(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]int, int]{
		{
			input:  [][]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}},
			output: 3,
		},
		{
			input:  [][]int{{0, 1}, {0, 1}, {0, 0}},
			output: 2,
		},
		{
			input:  [][]int{{1}, {1}},
			output: 2,
		},
	}
	for _, tc := range testcases {
		if got := minFlips(tc.input); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
