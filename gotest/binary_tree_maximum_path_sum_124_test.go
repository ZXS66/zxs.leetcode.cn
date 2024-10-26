package gotest

// https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150

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
func maxPathSum(root *TreeNode) int {
	val1, val2 := dfs(root)
	return max(val1, val2)
}

const minVal = -1001

// 返回 (以root为结尾的最大路径和（可继续连接）,不以root结尾的最大路径和)
func dfs(root *TreeNode) (int, int) {
	if root == nil {
		// -1000 <= Node.val <= 1000
		return minVal, minVal
	} else if root.Left == nil && root.Right == nil {
		return root.Val, root.Val
	}
	leftVal1, leftVal2 := dfs(root.Left)
	rightVal1, rightVal2 := dfs(root.Right)
	return max(max(leftVal1, rightVal1)+root.Val, root.Val), max(leftVal2, rightVal2, leftVal1+rightVal1+root.Val, leftVal1, rightVal1)
}

func TestMaxPathSum(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, int]{
		{
			input: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			output: 6,
		},
		{
			input: &TreeNode{
				Val:  -10,
				Left: &TreeNode{Val: 9},
				Right: &TreeNode{
					Val:   20,
					Left:  &TreeNode{Val: 15},
					Right: &TreeNode{Val: 7},
				},
			},
			output: 42,
		},
		{
			input: &TreeNode{
				Val:  -2,
				Left: &TreeNode{Val: -1},
			},
			output: -1,
		},
		{
			input: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: -2,
					Left: &TreeNode{
						Val:   -3,
						Left:  &TreeNode{Val: 1},
						Right: &TreeNode{Val: 3},
					},
				},
				Right: &TreeNode{
					Val:   -2,
					Right: &TreeNode{Val: -1},
				},
			},
			output: 3,
		},
		{
			input: &TreeNode{
				Val: -1,
				Left: &TreeNode{
					Val:  -2,
					Left: &TreeNode{Val: -6},
				},
				Right: &TreeNode{
					Val:   10,
					Left:  &TreeNode{Val: -3},
					Right: &TreeNode{Val: -6},
				},
			},
			output: 10,
		},
	}
	for _, tc := range testcases {
		if output := maxPathSum(tc.input); output != tc.output {
			t.Errorf("want %v, got %v", tc.output, output)
		}
	}
}
