package gotest

// https://leetcode.cn/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"testing"
)

func maxPoints(points [][]int) int {
	n := len(points)
	if n <= 2 {
		return n
	}
	ans := 0
	for i, p := range points {
		if ans >= n-i || ans > n/2 {
			break
		}
		cnt := map[int]int{}
		for _, q := range points[i+1:] {
			x, y := p[0]-q[0], p[1]-q[1]
			if x == 0 {
				y = 1
			} else if y == 0 {
				x = 1
			} else {
				if y < 0 {
					x, y = -x, -y
				}
				g := gcd(abs(x), abs(y))
				x /= g
				y /= g
			}
			cnt[y+x*20001]++
		}
		for _, c := range cnt {
			ans = max(ans, c+1)
		}
	}
	return ans
}
func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Test_maxPoints(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]int, int]{
		{
			input: [][]int{
				{1, 1}, {2, 2}, {3, 3},
			},
			output: 3,
		},
		{
			input: [][]int{
				{1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4},
			},
			output: 4,
		},
		{
			input: [][]int{
				{2, 3}, {3, 3}, {-5, 3},
			},
			output: 3,
		},
		{
			input: [][]int{
				{0, 0}, {4, 5}, {7, 8}, {8, 9}, {5, 6}, {3, 4}, {1, 1},
			},
			output: 5,
		},
		{
			input:  [][]int{{3, 3}, {1, 4}, {1, 1}, {2, 1}, {2, 2}},
			output: 3,
		},
		{
			input:  [][]int{{7, 3}, {19, 19}, {-16, 3}, {13, 17}, {-18, 1}, {-18, -17}, {13, -3}, {3, 7}, {-11, 12}, {7, 19}, {19, -12}, {20, -18}, {-16, -15}, {-10, -15}, {-16, -18}, {-14, -1}, {18, 10}, {-13, 8}, {7, -5}, {-4, -9}, {-11, 2}, {-9, -9}, {-5, -16}, {10, 14}, {-3, 4}, {1, -20}, {2, 16}, {0, 14}, {-14, 5}, {15, -11}, {3, 11}, {11, -10}, {-1, -7}, {16, 7}, {1, -11}, {-8, -3}, {1, -6}, {19, 7}, {3, 6}, {-1, -2}, {7, -3}, {-6, -8}, {7, 1}, {-15, 12}, {-17, 9}, {19, -9}, {1, 0}, {9, -10}, {6, 20}, {-12, -4}, {-16, -17}, {14, 3}, {0, -1}, {-18, 9}, {-15, 15}, {-3, -15}, {-5, 20}, {15, -14}, {9, -17}, {10, -14}, {-7, -11}, {14, 9}, {1, -1}, {15, 12}, {-5, -1}, {-17, -5}, {15, -2}, {-12, 11}, {19, -18}, {8, 7}, {-5, -3}, {-17, -1}, {-18, 13}, {15, -3}, {4, 18}, {-14, -15}, {15, 8}, {-18, -12}, {-15, 19}, {-9, 16}, {-9, 14}, {-12, -14}, {-2, -20}, {-3, -13}, {10, -7}, {-2, -10}, {9, 10}, {-1, 7}, {-17, -6}, {-15, 20}, {5, -17}, {6, -6}, {-11, -8}},
			output: 6,
		},
	}
	for _, tc := range testcases {
		if got := maxPoints(tc.input); got != tc.output {
			t.Errorf("maxPoints(%v) = %v, want %v", tc.input, got, tc.output)
		}
	}
}
