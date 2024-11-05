package gotest

// https://leetcode.cn/problems/find-the-winning-player-in-coin-game/description/
import (
	"testing"
)

func losingPlayer(x int, y int) string {
	// 两名玩家都采取 最优 策略，请你返回游戏的赢家。
	// 不就有且仅有一种拿法吗：1×75+4×10=115？？
	// 明天的题目，会有多个面额的硬币？？
	a, b := x, y/4
	var picks int
	if b < a {
		picks = b
	} else {
		picks = a
	}
	if picks%2 == 1 {
		return "Alice"
	} else {
		return "Bob"
	}
}

func TestLosingPlayer(t *testing.T) {
	type args struct {
		x int
		y int
	}
	testcases := []LeetcodeTestCase[args, string]{
		{
			input: args{
				x: 2,
				y: 7,
			},
			output: "Alice",
		},
		{
			input: args{
				x: 4,
				y: 11,
			},
			output: "Bob",
		},
	}
	for _, tc := range testcases {
		if res := losingPlayer(tc.input.x, tc.input.y); res != tc.output {
			t.Errorf("losingPlayer(%v, %v) = %v, want %v", tc.input.x, tc.input.y, res, tc.output)
		}
	}
}
