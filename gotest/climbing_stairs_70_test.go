package gotest

// https://leetcode.cn/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

import "testing"

func climbStairs(n int) int {
	// if n == 1 || n == 2 {
	// 	return n
	// } else {
	// 	return climbStairs(n-1) + climbStairs(n-2)
	// }
	memo := make(map[int]int)
	memo[1] = 1
	memo[2] = 2
	for i := 3; i <= n; i++ {
		memo[i] = memo[i-1] + memo[i-2]
	}
	return memo[n]
}

func TestClimbStairs(t *testing.T) {
	testcases := []LeetcodeTestCase[int, int]{
		{
			input:  2,
			output: 2,
		},
		{
			input:  3,
			output: 3,
		},
	}
	for _, tc := range testcases {
		if got := climbStairs(tc.input); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
