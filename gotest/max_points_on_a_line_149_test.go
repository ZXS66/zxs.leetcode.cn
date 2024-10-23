package gotest

// https://leetcode.cn/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"fmt"
	"strings"
	"testing"
)

func maxPoints(points [][]int) int {
	if len(points) <= 2 {
		return len(points)
	}
	degree := make(map[float64]string)
	vertical_points := make(map[int]string)
	const delimiter = "\n"
	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			x1, y1 := points[i][0], points[i][1]
			x2, y2 := points[j][0], points[j][1]
			str1 := fmt.Sprintf("%d,%d", x1, y1)
			str2 := fmt.Sprintf("%d,%d", x2, y2)
			if x1 != x2 {
				dg := float64(y2-y1) / float64(x2-x1)
				value := degree[dg]
				if !strings.Contains(value, str1) {
					value += str1 + delimiter
				}
				if !strings.Contains(value, str2) {
					value += str2 + delimiter
				}
				degree[dg] = value
				if strings.Count(value, delimiter) > 2 {
					fmt.Printf("[%v, %v]", dg, value)
				}
			} else {
				value := vertical_points[x1]
				if !strings.Contains(value, str1) {
					value += str1 + delimiter
				}
				if !strings.Contains(value, str2) {
					value += str2 + delimiter
				}
				vertical_points[x1] = value
			}
		}
	}
	// 至少两个点（才能确定一条直线）
	ans := 2
	for _, v := range vertical_points {
		ans = max(ans, strings.Count(v, delimiter))
	}
	for _, v := range degree {
		ans = max(ans, strings.Count(v, delimiter))
	}
	return ans
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
		// {
		// 	input: [][]int{
		// 		{0, 0}, {94911151, 94911150}, {94911152, 94911151},
		// 	},
		// 	output: 2,
		// },
		{
			input: [][]int{
				{0, 0}, {4, 5}, {7, 8}, {8, 9}, {5, 6}, {3, 4}, {1, 1},
			},
			output: 3,
		},
	}
	for _, tc := range testcases {
		if got := maxPoints(tc.input); got != tc.output {
			t.Errorf("maxPoints(%v) = %v, want %v", tc.input, got, tc.output)
		}
	}
}
