package gotest

// https://leetcode.cn/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

import (
	// "math"
	"testing"
)

func myPow(x float64, n int) float64 {
	// return math.Pow(x, float64(n))
	if n < 0 {
		return 1 / myPow(x, -n)
	} else if n == 0 {
		return 1
	}
	if (n % 2) == 0 {
		return myPow(x*x, n/2)
	} else {
		return x * myPow(x, n-1)
	}
}

func Test_myPow(t *testing.T) {
	type args struct {
		x float64
		n int
	}
	testcases := []LeetcodeTestCase[args, float64]{
		{
			input: args{
				x: 2.00000,
				n: 10,
			},
			output: 1024.00000,
		},
		// {
		// 	input: args{
		// 		x: 2.10000,
		// 		n: 3,
		// 	},
		// 	output: 9.26100,
		// },
		{
			input: args{
				x: 2.00000,
				n: -2,
			},
			output: 0.25000,
		},
	}
	for _, tc := range testcases {
		t.Run("Test myPow", func(t *testing.T) {
			got := myPow(tc.input.x, tc.input.n)
			if got != tc.output {
				t.Errorf("myPow(%v, %v) = %v, want %v", tc.input.x, tc.input.n, got, tc.output)
			}
		})
	}
}
