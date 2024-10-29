package gotest

// https://leetcode.cn/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150
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
func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	if root.Left != nil && root.Left.Val >= root.Val {
		return false
	}
	if root.Right != nil && root.Right.Val <= root.Val {
		return false
	}
	leftValues := getValues(root.Left)
	for _, v := range leftValues {
		if v >= root.Val {
			return false
		}
	}
	rightValues := getValues(root.Right)
	for _, v := range rightValues {
		if v <= root.Val {
			return false
		}
	}
	return isValidBST(root.Left) && isValidBST(root.Right)
}

// var getValues func(node *TreeNode) []int
func getValues(node *TreeNode) []int {
	if node == nil {
		return []int{}
	}
	return append(append(getValues(node.Left), node.Val), getValues(node.Right)...)
}

func TestIsValidBST(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, bool]{
		{
			input: &TreeNode{
				Val:   2,
				Left:  &TreeNode{Val: 1},
				Right: &TreeNode{Val: 3},
			},
			output: true,
		},
		{
			input: &TreeNode{
				Val:  5,
				Left: &TreeNode{Val: 1},
				Right: &TreeNode{
					Val:   4,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 6},
				},
			},
			output: false,
		},
		{
			input: &TreeNode{
				Val:  5,
				Left: &TreeNode{Val: 4},
				Right: &TreeNode{
					Val:   6,
					Left:  &TreeNode{Val: 3},
					Right: &TreeNode{Val: 7},
				},
			},
			output: false,
		},
	}
	for _, tc := range testcases {
		if got := isValidBST(tc.input); got != tc.output {
			t.Errorf("input: %v, expected: %v, got: %v", tc.input, tc.output, got)
		}
	}
}
