package gotest

// https://leetcode.cn/problems/shopping-offers/description/
import (
	"testing"
)

func shoppingOffers(price []int, special [][]int, needs []int) int {
	// 不可以购买超出待购清单的物品！！
	m, n := len(special), len(price)
	maxPrice := 0
	// 计算不用礼包的价格
	for i := 0; i < n; i++ {
		maxPrice += price[i] * needs[i]
	}
	maxSpecials := make([]int, m) // 每个礼包的购买数量
	// 计算每个礼包最多购买数量
	for i := 0; i < m; i++ {
		// 初始礼包购买数量，其价格不超过单独购买单品价格
		if special[i][n] != 0 {
			maxSpecials[i] = maxPrice / special[i][n]
		} else {
			// 免费礼包？？谁出的测试用例…
			maxSpecials[i] = 10 // needs[i] <= 10
		}
		for j := n - 1; j >= 0; j-- {
			// 礼包中单品数量不能超过需求数量
			if special[i][j] != 0 {
				maxSpecials[i] = min(maxSpecials[i], (needs[j])/special[i][j])
			}
		}
	}
	// 遍历所有不同礼包数量的可能性组合，得出满足购买购物清单指定数量的物品的同时，价格最低
	ans := maxPrice
	calculateFee := func(specialAmount []int) int {
		goodAmount := make(map[int]int)
		specialFee := 0
		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				goodAmount[j] += specialAmount[i] * special[i][j]
			}
			specialFee += specialAmount[i] * special[i][n]
		}
		totalFee := specialFee
		for i := 0; i < n; i++ {
			if goodAmount[i] > needs[i] {
				// 超出需求数量，无法满足，返回最大价格
				return maxPrice
			}
			totalFee += (needs[i] - goodAmount[i]) * price[i]
		}
		return totalFee
	}
	var searchSpecialCombination func(specialAmount []int)
	searchSpecialCombination = func(specialAmount []int) {
		fee := calculateFee(specialAmount)
		if fee < ans {
			ans = fee
		}
		for i := 0; i < m; i++ {
			// 剪枝，如果当前礼包数量已经用完，则不再尝试
			if specialAmount[i] == 0 {
				continue
			}
			// 尝试当前礼包数量-1，并更新剩余需求数量
			specialAmount[i]--
			searchSpecialCombination(specialAmount)
			specialAmount[i]++
		}
	}
	searchSpecialCombination(maxSpecials)
	return ans
}

func TestShoppingOffers(t *testing.T) {
	type args struct {
		price   []int
		special [][]int
		needs   []int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				price:   []int{2, 5},
				special: [][]int{{3, 0, 5}, {1, 2, 10}},
				needs:   []int{3, 2},
			},
			output: 14,
		},
		{
			input: args{
				price:   []int{2, 3, 4},
				special: [][]int{{1, 1, 0, 4}, {2, 2, 1, 9}},
				needs:   []int{1, 2, 1},
			},
			output: 11,
		},
		{
			input: args{
				price:   []int{1, 1, 1},
				special: [][]int{{1, 1, 0, 0}, {2, 2, 1, 9}},
				needs:   []int{1, 1, 0},
			},
			output: 0,
		},
	}
	for _, tc := range testcases {
		got := shoppingOffers(tc.input.price, tc.input.special, tc.input.needs)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
