package gotest

// https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150

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

func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	dump := root
	flatten(root.Right)
	flatten(root.Left)
	right := root.Right
	if root.Left != nil {
		root.Right = root.Left
		root.Left = nil
		for root.Right != nil {
			root = root.Right
		}
		root.Right = right
	}
	if right == nil {
		root.Right = right
	}
	root = dump // 重新赋值
}

func Test_0114(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, int]{
		{
			input: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
					Right: &TreeNode{
						Val: 4,
					},
				},
				Right: &TreeNode{
					Val: 5,
					Right: &TreeNode{
						Val: 6,
					},
				},
			},
			output: 6,
		},
		{
			input:  nil,
			output: 0,
		},
		{
			input: &TreeNode{
				Val: 1,
			},
			output: 1,
		},
	}
	for _, tc := range testcases {
		flatten(tc.input)
		length := 0
		for tc.input != nil {
			length++
			tc.input = tc.input.Right
		}
		if length != tc.output {
			t.Errorf("want %v, got %v", tc.output, length)
		}
	}
}
