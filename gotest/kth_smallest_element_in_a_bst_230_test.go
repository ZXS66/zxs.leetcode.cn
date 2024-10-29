package gotest

// https://leetcode.cn/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150
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
func kthSmallest(root *TreeNode, k int) int {
	var getValues func(node *TreeNode) []int
	getValues = func(node *TreeNode) []int {
		if node == nil {
			return []int{}
		}
		return append(append(getValues(node.Left), node.Val), getValues(node.Right)...)
	}
	values := getValues(root)
	slices.Sort(values)
	return values[k-1]
}

func Test_kthSmallest(t *testing.T) {
	type args struct {
		root *TreeNode
		k    int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				root: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:   1,
						Right: &TreeNode{Val: 2},
					},
					Right: &TreeNode{Val: 4},
				},
				k: 1,
			},
			output: 1,
		},
		{
			input: args{
				root: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val:   3,
						Left:  &TreeNode{Val: 2, Left: &TreeNode{Val: 1}},
						Right: &TreeNode{Val: 4},
					},
					Right: &TreeNode{Val: 6},
				},
				k: 3,
			},
			output: 3,
		},
	}
	for _, tc := range testcases {
		if got := kthSmallest(tc.input.root, tc.input.k); got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
