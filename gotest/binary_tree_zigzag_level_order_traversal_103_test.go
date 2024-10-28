package gotest

// https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"reflect"
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
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	ans := [][]int{
		{root.Val},
	}
	ltr := false // left to right
	for queue := []*TreeNode{root}; len(queue) > 0; {
		levelValues := []int{}
		nextQueue := make([]*TreeNode, 0)
		for _, item := range queue {
			if item.Left != nil {
				levelValues = append(levelValues, item.Left.Val)
				nextQueue = append(nextQueue, item.Left)
			}
			if item.Right != nil {
				levelValues = append(levelValues, item.Right.Val)
				nextQueue = append(nextQueue, item.Right)
			}
		}
		if len(levelValues) > 0 {
			if !ltr {
				slices.Reverse(levelValues)
			}
			ans = append(ans, levelValues)
		}
		queue = nextQueue
		ltr = !ltr
	}
	return ans
}

func TestZigzagLevelOrder(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, [][]int]{
		{
			input:  &TreeNode{Val: 3, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20, Left: &TreeNode{Val: 15}, Right: &TreeNode{Val: 7}}},
			output: [][]int{{3}, {20, 9}, {15, 7}},
		},
		{
			input:  nil,
			output: [][]int{},
		},
		{
			input:  &TreeNode{Val: 1},
			output: [][]int{{1}},
		},
	}
	for _, tc := range testcases {
		if got := zigzagLevelOrder(tc.input); !reflect.DeepEqual(got, tc.output) {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
