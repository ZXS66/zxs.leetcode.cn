package gotest

import "testing"

// https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/description/

func countCompleteDayPairs(hours []int) int64 {
	hour_count := [24]int{}
	var ans int64 = 0
	for _, h := range hours {
		ans += int64(hour_count[(24-h%24)%24])
		hour_count[h%24]++
	}
	return ans
}

func TestCountCompleteDayPairs(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int64]{
		{
			input:  []int{12, 12, 30, 24, 24},
			output: 2,
		},
		{
			input:  []int{72, 48, 24, 3},
			output: 3,
		},
	}
	for _, tc := range testcases {
		t.Run("TestCountCompleteDayPairs", func(t *testing.T) {
			output := countCompleteDayPairs(tc.input)
			if output != tc.output {
				t.Fatalf("input %v, output %v, expect %v", tc.input, output, tc.output)
			}
		})
	}
}
