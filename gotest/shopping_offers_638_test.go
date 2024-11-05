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
		{
			input: args{
				price:   []int{9, 6, 1, 5, 3, 4},
				special: [][]int{{1, 2, 2, 1, 0, 4, 14}, {6, 3, 4, 0, 0, 1, 16}, {4, 5, 6, 6, 2, 4, 26}, {1, 1, 4, 3, 4, 3, 15}, {4, 2, 5, 4, 4, 5, 15}, {4, 0, 0, 2, 3, 5, 13}, {2, 4, 6, 4, 3, 5, 7}, {3, 3, 4, 2, 2, 6, 21}, {0, 3, 0, 2, 3, 3, 15}, {0, 2, 4, 2, 2, 5, 24}, {4, 1, 5, 4, 5, 4, 25}, {6, 0, 5, 0, 1, 1, 14}, {4, 0, 5, 2, 1, 5, 8}, {4, 1, 4, 4, 3, 1, 10}, {4, 4, 2, 1, 5, 0, 14}, {2, 4, 4, 1, 3, 1, 16}, {4, 2, 3, 1, 2, 1, 26}, {2, 4, 1, 6, 5, 3, 2}, {0, 2, 0, 4, 0, 0, 19}, {3, 1, 6, 3, 3, 1, 23}, {6, 2, 3, 2, 4, 4, 16}, {5, 3, 5, 5, 0, 4, 5}, {5, 0, 4, 3, 0, 2, 20}, {5, 3, 1, 2, 2, 5, 8}, {3, 0, 6, 1, 0, 2, 10}, {5, 6, 6, 1, 0, 4, 12}, {0, 6, 6, 4, 6, 4, 21}, {0, 4, 6, 5, 0, 0, 22}, {0, 4, 2, 4, 4, 6, 16}, {4, 2, 1, 0, 6, 5, 14}, {0, 1, 3, 5, 0, 3, 8}, {5, 5, 3, 3, 2, 0, 4}, {1, 0, 3, 6, 2, 3, 18}, {4, 2, 6, 2, 2, 5, 2}, {0, 2, 5, 5, 3, 6, 12}, {1, 0, 6, 6, 5, 0, 10}, {6, 0, 0, 5, 5, 1, 24}, {1, 4, 6, 5, 6, 3, 19}, {2, 2, 4, 2, 4, 2, 20}, {5, 6, 1, 4, 0, 5, 3}, {3, 3, 2, 2, 1, 0, 14}, {0, 1, 3, 6, 5, 0, 9}, {5, 3, 6, 5, 3, 3, 11}, {5, 3, 3, 1, 0, 2, 26}, {0, 1, 1, 4, 2, 1, 16}, {4, 2, 3, 2, 1, 4, 6}, {0, 2, 1, 3, 3, 5, 15}, {5, 6, 4, 1, 2, 5, 18}, {1, 0, 0, 1, 6, 1, 16}, {2, 0, 6, 6, 2, 2, 17}, {4, 4, 0, 2, 4, 6, 12}, {0, 5, 2, 5, 4, 6, 6}, {5, 2, 1, 6, 2, 1, 24}, {2, 0, 2, 2, 0, 1, 14}, {1, 1, 0, 5, 3, 5, 16}, {0, 2, 3, 5, 5, 5, 6}, {3, 2, 0, 6, 4, 6, 8}, {4, 0, 1, 4, 5, 1, 6}, {5, 0, 5, 6, 6, 3, 7}, {2, 6, 0, 0, 2, 1, 25}, {0, 4, 6, 1, 4, 4, 6}, {6, 3, 1, 4, 1, 1, 24}, {6, 2, 1, 2, 1, 4, 4}, {0, 1, 2, 3, 0, 1, 3}, {0, 2, 5, 6, 5, 2, 13}, {2, 6, 4, 2, 2, 3, 17}, {3, 4, 5, 0, 5, 4, 20}, {6, 2, 3, 4, 1, 3, 4}, {6, 4, 0, 0, 0, 5, 16}, {3, 1, 2, 5, 0, 6, 11}, {1, 3, 2, 2, 5, 6, 14}, {1, 3, 4, 5, 3, 5, 18}, {2, 1, 1, 2, 6, 1, 1}, {4, 0, 4, 0, 6, 6, 8}, {4, 6, 0, 5, 0, 2, 1}, {3, 1, 0, 5, 3, 2, 26}, {4, 0, 4, 0, 6, 6, 6}, {5, 0, 0, 0, 0, 4, 26}, {4, 3, 2, 2, 0, 2, 14}, {5, 2, 4, 0, 2, 2, 26}, {3, 4, 6, 0, 2, 4, 25}, {2, 1, 5, 5, 1, 3, 26}, {0, 5, 2, 4, 0, 2, 24}, {5, 2, 5, 4, 5, 0, 1}, {5, 3, 0, 1, 5, 4, 15}, {6, 1, 5, 1, 2, 1, 21}, {2, 5, 1, 2, 1, 4, 15}, {1, 4, 4, 0, 0, 0, 1}, {5, 0, 6, 1, 1, 4, 22}, {0, 1, 1, 6, 1, 4, 1}, {1, 6, 0, 3, 2, 2, 17}, {3, 4, 3, 3, 1, 5, 17}, {1, 5, 5, 4, 5, 2, 27}, {0, 6, 5, 5, 0, 0, 26}, {1, 4, 0, 3, 1, 0, 13}, {1, 0, 3, 5, 2, 4, 5}, {2, 2, 2, 3, 0, 0, 11}, {3, 2, 2, 1, 1, 1, 6}, {6, 6, 1, 1, 1, 6, 26}, {1, 5, 1, 2, 5, 2, 12}},
				needs:   []int{6, 6, 6, 1, 6, 6},
			},
			output: 11,
		},
	}
	for _, tc := range testcases {
		got := shoppingOffers(tc.input.price, tc.input.special, tc.input.needs)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
