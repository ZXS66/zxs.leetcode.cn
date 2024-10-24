package gotest

// https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/

import (
	"testing"
)

func findWinningPlayer(skills []int, k int) int {
	// 方案一：模拟法（会超时！！！）
	// queue := make([]int, 0)        // [player index]
	// scorecard := make(map[int]int) // [player index, score]

	// idx_of_max_skill := 0
	// // initialize player queue
	// for i := range len(skills) {
	// 	queue = append(queue, i)
	// 	if skills[i] > skills[idx_of_max_skill] {
	// 		idx_of_max_skill = i
	// 	}
	// }
	// if idx_of_max_skill < k {
	// 	// winner: max skill player
	// 	return idx_of_max_skill
	// }
	// for {
	// 	idx_a, idx_b := queue[0], queue[1]
	// 	if skills[idx_a] > skills[idx_b] {
	// 		// winner: a
	// 		queue = append([]int{idx_a}, queue[2:]...)
	// 		queue = append(queue, idx_b)
	// 		scorecard[idx_a]++
	// 		if scorecard[idx_a] >= k {
	// 			return idx_a
	// 		}
	// 	} else {
	// 		// winner: b
	// 		queue = append([]int{idx_b}, queue[2:]...)
	// 		queue = append(queue, idx_a)
	// 		scorecard[idx_b]++
	// 		if scorecard[idx_b] >= k {
	// 			return idx_b
	// 		}
	// 	}
	// }
	// 方案二（优化版）
	if k == 1 {
		if skills[0] > skills[1] {
			return 0
		} else {
			return 1
		}
	}
	max_skill := 0 // 1 <= skills[i] <= 10^6
	idx_of_max_skill := 0
	for i, v := range skills {
		if v > max_skill {
			max_skill = v
			idx_of_max_skill = i
		}
		if i >= 2 {
			// compare times == i
			wins_of_max_skill := 0
			if idx_of_max_skill == 0 {
				wins_of_max_skill = i
			} else {
				wins_of_max_skill = (i - idx_of_max_skill + 1)
			}
			if wins_of_max_skill >= k {
				return idx_of_max_skill
			}
		}
	}
	return idx_of_max_skill
	// 以上方案还是太复杂，更优雅的请参考灵神：https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/solutions/2805251/da-lei-tai-pythonjavacgo-by-endlesscheng-juk1/
}

func TestFindWinningPlayer(t *testing.T) {
	type args struct {
		skills []int
		k      int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				skills: []int{4, 2, 6, 3, 9},
				k:      2,
			},
			output: 2,
		},
		{
			input: args{
				skills: []int{2, 5, 4},
				k:      3,
			},
			output: 1,
		},
		{
			input: args{
				skills: []int{16, 4, 7, 17},
				k:      562084119,
			},
			output: 3,
		},
		{
			input: args{
				skills: []int{5, 3, 1, 6, 8},
				k:      3,
			},
			output: 4,
		},
		{
			input: args{
				skills: []int{10, 2, 3, 12, 9, 1},
				k:      2,
			},
			output: 0,
		},
	}
	for _, tt := range testcases {
		if got := findWinningPlayer(tt.input.skills, tt.input.k); got != tt.output {
			t.Errorf("findWinningPlayer() = %v, want %v", got, tt.output)
		}
	}
}
