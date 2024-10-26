package gotest

// https://leetcode.cn/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

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

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	if root.Val == targetSum && root.Left == nil && root.Right == nil {
		// 叶子节点，且Val 与 targetSum 相等，返回true
		return true
	} else if root.Left != nil && hasPathSum(root.Left, targetSum-root.Val) {
		// 左子树存在路径，返回true
		return true
	} else if root.Right != nil && hasPathSum(root.Right, targetSum-root.Val) {
		// 右子树存在路径，返回true
		return true
	}
	return false
}

func Test_hasPathSum(t *testing.T) {
	type args struct {
		root      *TreeNode
		targetSum int
	}
	testcases := []LeetcodeTestCase[args, bool]{
		{
			input: args{
				root: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val:   11,
							Left:  &TreeNode{Val: 7},
							Right: &TreeNode{Val: 2},
						},
					},
					Right: &TreeNode{
						Val:  8,
						Left: &TreeNode{Val: 13},
						Right: &TreeNode{
							Val:   4,
							Right: &TreeNode{Val: 1},
						},
					},
				},
				targetSum: 22,
			},
			output: true,
		},
		{
			input: args{
				root: &TreeNode{
					Val:   1,
					Left:  &TreeNode{Val: 2},
					Right: &TreeNode{Val: 3},
				},
				targetSum: 5,
			},
			output: false,
		},
		{
			input:  args{nil, 0},
			output: false,
		},
	}
	for _, tc := range testcases {
		if got := hasPathSum(tc.input.root, tc.input.targetSum); got != tc.output {
			t.Errorf("got %v, want %v", got, tc.output)
		}
	}
}
