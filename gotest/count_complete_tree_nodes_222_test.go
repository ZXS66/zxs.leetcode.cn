package gotest

// https://leetcode.cn/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
import (
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
func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + countNodes(root.Left) + countNodes(root.Right)
}

func Test_countNodes(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, int]{
		{
			input: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 4},
					Right: &TreeNode{Val: 5},
				},
				Right: &TreeNode{
					Val:  3,
					Left: &TreeNode{Val: 6},
				},
			},
			output: 6,
		},
		{
			input:  nil,
			output: 0,
		},
		{
			input:  &TreeNode{Val: 1},
			output: 1,
		},
	}
	for _, tc := range testcases {
		if got := countNodes(tc.input); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
