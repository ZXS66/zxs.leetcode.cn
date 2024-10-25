package gotest

// https://leetcode.cn/problems/maximum-total-reward-using-operations-i/description/

/**

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/solutions/2805413/bitset-you-hua-0-1-bei-bao-by-endlessche-m1xn/

对于 rewardValues 中的数，如果先选大的，就没法再选小的，所以按照从小到大的顺序选是最优的。

设 m=max(rewardValues)，如果数组中包含 m−1，则答案为 2m−1（因为这是答案的上界），无需计算 DP。


*/

import (
	"math/big"
	"slices"
	"testing"
)

func maxTotalRewardII(rewardValues []int) int {
	m := slices.Max(rewardValues)
	has := map[int]bool{}
	for _, v := range rewardValues {
		if v == m-1 {
			return m*2 - 1
		}
		if has[v] {
			continue
		}
		if has[m-1-v] {
			return m*2 - 1
		}
		has[v] = true
	}

	slices.Sort(rewardValues)
	rewardValues = slices.Compact(rewardValues) // 去重

	one := big.NewInt(1)
	f := big.NewInt(1)
	p := new(big.Int)
	for _, v := range rewardValues {
		mask := p.Sub(p.Lsh(one, uint(v)), one)
		f.Or(f, p.Lsh(p.And(f, mask), uint(v)))
	}
	return f.BitLen() - 1
}

func TestMaxTotalRewardII(t *testing.T) {
	testcases := []LeetcodeTestCase[[]int, int]{
		{
			input:  []int{1, 1, 3, 3},
			output: 4,
		},
		{
			input:  []int{1, 6, 4, 3, 2},
			output: 11,
		},
		{
			input:  []int{22, 83, 54, 89, 29, 86, 78, 51, 49, 99, 22, 54, 9, 82, 42, 40, 94, 44, 41, 1, 5, 86, 21, 37, 79, 85, 34, 5, 76, 76, 31, 83, 15, 10, 43, 34, 45, 55, 99, 34, 99, 64, 46, 21, 18, 98, 11, 24, 80, 6, 3, 71, 65, 15, 88, 40, 34, 62, 3, 95, 41},
			output: 197,
		},
	}
	for _, testcase := range testcases {
		if output := maxTotalRewardII(testcase.input); output != testcase.output {
			t.Errorf("maxTotalReward(%v) = %v, want %v", testcase.input, output, testcase.output)
		}
	}
}
