package gotest

// https://leetcode.cn/problems/redundant-connection/description/
import (
	"reflect"
	"testing"
)

func findRedundantConnection(edges [][]int) []int {
	parent := make([]int, len(edges)+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(from, to int) bool {
		x, y := find(from), find(to)
		if x == y {
			return false
		}
		parent[x] = y
		return true
	}
	for _, e := range edges {
		if !union(e[0], e[1]) {
			return e
		}
	}
	return nil
}

func TestFindRedundantConnection(t *testing.T) {
	testcases := []LeetcodeTestCase[[][]int, []int]{
		{
			input:  [][]int{{1, 2}, {1, 3}, {2, 3}},
			output: []int{2, 3},
		},
		{
			input:  [][]int{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}},
			output: []int{1, 4},
		},
		{
			input:  [][]int{{9, 10}, {5, 8}, {2, 6}, {1, 5}, {3, 8}, {4, 9}, {8, 10}, {4, 10}, {6, 8}, {7, 9}},
			output: []int{4, 10},
		},
	}
	for _, tc := range testcases {
		got := findRedundantConnection(tc.input)
		if !reflect.DeepEqual(got, tc.output) {
			t.Errorf("findRedundantConnection(%v) = %v, want %v", tc.input, got, tc.output)
		}
	}
}
