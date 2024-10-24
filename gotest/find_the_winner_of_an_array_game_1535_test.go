package gotest

// https://leetcode.cn/problems/find-the-winner-of-an-array-game/description/

import (
	"testing"
)

func getWinner(arr []int, k int) int {
	winner := arr[0] // assume the first element is the winner
	wins := 0        // times of wins of the winner
	for i := 1; i < len(arr) && wins < k; i++ {
		if arr[i] > winner {
			// found new winner
			winner = arr[i]
			wins = 1
		} else {
			wins++
		}
	}
	return winner
}

func Test_getWinner(t *testing.T) {
	type args = struct {
		arr []int
		k   int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				arr: []int{2, 1, 3, 5, 4, 6, 7},
				k:   2,
			},
			output: 5,
		},
		{
			input: args{
				arr: []int{3, 2, 1},
				k:   10,
			},
			output: 3,
		},
		{
			input: args{
				arr: []int{1, 9, 8, 2, 3, 7, 6, 4, 5},
				k:   7,
			},
			output: 9,
		},
		{
			input: args{
				arr: []int{1, 11, 22, 33, 44, 55, 66, 77, 88, 99},
				k:   1000000000,
			},
			output: 99,
		},
	}
	for _, tc := range testcases {
		if got := getWinner(tc.input.arr, tc.input.k); got != tc.output {
			t.Errorf("getWinner(%v, %v) = %v, want %v", tc.input.arr, tc.input.k, got, tc.output)
		}
	}
}
