package gotest

// https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
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
func averageOfLevels(root *TreeNode) []float64 {
	ans := []float64{}
	for queue := []*TreeNode{root}; len(queue) > 0; {
		sum := 0
		nextQueue := make([]*TreeNode, 0)
		for _, item := range queue {
			sum += item.Val
			if item.Left != nil {
				nextQueue = append(nextQueue, item.Left)
			}
			if item.Right != nil {
				nextQueue = append(nextQueue, item.Right)
			}
		}
		ans = append(ans, float64(sum)/float64(len(queue)))
		queue = nextQueue
	}
	return ans
}

func TestAverageOfLevels(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, []float64]{
		{
			input: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 9,
				},
				Right: &TreeNode{
					Val:   20,
					Left:  &TreeNode{Val: 15},
					Right: &TreeNode{Val: 7},
				},
			},
			output: []float64{3, 14.5, 11},
		},
		{
			input: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val:   9,
					Left:  &TreeNode{Val: 15},
					Right: &TreeNode{Val: 7},
				},
				Right: &TreeNode{
					Val: 20,
				},
			},
			output: []float64{3, 14.5, 11},
		},
	}
	for _, tc := range testcases {
		if got := averageOfLevels(tc.input); !reflect.DeepEqual(tc.output, got) {
			t.Errorf("expected %v, actual %v", tc.output, got)
		}
	}
}
