package gotest

// https://leetcode.cn/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150
import (
	"slices"
	"testing"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getMinimumDifference(root *TreeNode) int {
	var getValues func(node *TreeNode) []int
	getValues = func(node *TreeNode) []int {
		if node == nil {
			return []int{}
		}
		return append(append(getValues(node.Left), node.Val), getValues(node.Right)...)
	}
	values := getValues(root)
	slices.Sort(values)
	minDistance := values[1] - values[0]
	if minDistance < 0 {
		// 差值是一个正数，其数值等于两值之差的绝对值。
		minDistance = -minDistance
	}
	for i := 2; i < len(values); i++ {
		distance := values[i] - values[i-1]
		if distance < 0 {
			distance = -distance
		}
		if distance < minDistance {
			minDistance = distance
		}
	}
	return minDistance
}

func TestGetMinimumDifference(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, int]{
		{
			input: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{Val: 6},
			},
			output: 1,
		},
		{
			input: &TreeNode{
				Val:  1,
				Left: &TreeNode{Val: 0},
				Right: &TreeNode{
					Val:   48,
					Left:  &TreeNode{Val: 12},
					Right: &TreeNode{Val: 49},
				},
			},
			output: 1,
		},
	}
	for _, tc := range testcases {
		if got := getMinimumDifference(tc.input); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
