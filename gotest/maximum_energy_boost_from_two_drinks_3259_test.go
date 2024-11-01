package gotest

// https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/description/
import (
	"testing"
)

func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
	n := len(energyDrinkA)
	c := [2][]int{energyDrinkA, energyDrinkB}
	memo := make([][2]int64, n)
	var dfs func(int, int) int64
	dfs = func(i, j int) int64 {
		if i < 0 {
			return 0
		}
		p := &memo[i][j]
		if *p == 0 { // 首次计算
			*p = max(dfs(i-1, j), dfs(i-2, j^1)) + int64(c[j][i])
		}
		return *p
	}
	return max(dfs(n-1, 0), dfs(n-1, 1))
}

func TestMaxEnergyBoost(t *testing.T) {
	type args struct {
		energyDrinkA []int
		energyDrinkB []int
	}
	testcases := []LeetcodeTestCase[args, int64]{
		{
			input: args{
				energyDrinkA: []int{1, 3, 1},
				energyDrinkB: []int{3, 1, 1},
			},
			output: 5,
		},
		{
			input: args{
				energyDrinkA: []int{4, 1, 1},
				energyDrinkB: []int{1, 1, 3},
			},
			output: 7,
		},
	}
	for _, tc := range testcases {
		got := maxEnergyBoost(tc.input.energyDrinkA, tc.input.energyDrinkB)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
