package gotest

// https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"reflect"
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
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	ans := []int{root.Val}
	for queue := []*TreeNode{root}; len(queue) > 0; {
		nextQueue := make([]*TreeNode, 0)
		for _, item := range queue {
			if item.Left != nil {
				nextQueue = append(nextQueue, item.Left)
			}
			if item.Right != nil {
				nextQueue = append(nextQueue, item.Right)
			}
		}
		if len(nextQueue) == 0 {
			break
		}
		ans = append(ans, nextQueue[len(nextQueue)-1].Val)
		queue = nextQueue
	}
	return ans
}

func TestRightSideView(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, []int]{
		{
			input: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val: 4,
					},
				},
			},
			output: []int{1, 3, 4},
		},
		{
			input: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 3,
				},
			},
			output: []int{1, 3},
		},
		{
			input:  nil,
			output: []int{},
		},
	}
	for _, tc := range testcases {
		if got := rightSideView(tc.input); !reflect.DeepEqual(got, tc.output) {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
