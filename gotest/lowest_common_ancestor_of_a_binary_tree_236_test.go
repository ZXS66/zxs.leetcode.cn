package gotest

// https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
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
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// 所有 Node.val 互不相同 。
	// p != q
	// p 和 q 均存在于给定的二叉树中。
	pPath := searchPath(root, p)
	qPath := searchPath(root, q)
	var ans *TreeNode
	for pLen, qLen := len(pPath)-1, len(qPath)-1; pLen >= 0 && qLen >= 0 && pPath[pLen].Val == qPath[qLen].Val; pLen, qLen = pLen-1, qLen-1 {
		ans = pPath[pLen]
	}
	return ans
}

func searchPath(root, target *TreeNode) []*TreeNode {
	if root == nil {
		return nil
	}
	exist := root.Val == target.Val
	if exist {
		return []*TreeNode{root}
	}
	leftPath := searchPath(root.Left, target)
	if len(leftPath) > 0 {
		return append(leftPath, root)
	}
	rightPath := searchPath(root.Right, target)
	if len(rightPath) > 0 {
		return append(rightPath, root)
	}
	return nil
}

func TestLowestCommonAncestor(t *testing.T) {
	type args struct {
		root, p, q *TreeNode
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				&TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:  5,
						Left: &TreeNode{Val: 6},
						Right: &TreeNode{
							Val:   2,
							Left:  &TreeNode{Val: 7},
							Right: &TreeNode{Val: 4},
						},
					},
					Right: &TreeNode{
						Val:   1,
						Left:  &TreeNode{Val: 0},
						Right: &TreeNode{Val: 8},
					},
				},
				&TreeNode{Val: 5},
				&TreeNode{Val: 1},
			},
			output: 3,
		},
		{
			input: args{
				&TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val:  5,
						Left: &TreeNode{Val: 6},
						Right: &TreeNode{
							Val:   2,
							Left:  &TreeNode{Val: 7},
							Right: &TreeNode{Val: 4},
						},
					},
					Right: &TreeNode{
						Val:   1,
						Left:  &TreeNode{Val: 0},
						Right: &TreeNode{Val: 8},
					},
				},
				&TreeNode{Val: 5},
				&TreeNode{Val: 4},
			},
			output: 5,
		},
		{
			input: args{
				&TreeNode{Val: 1, Left: &TreeNode{Val: 2}},
				&TreeNode{Val: 1},
				&TreeNode{Val: 2},
			},
			output: 1,
		},
	}
	for _, tc := range testcases {
		if output := lowestCommonAncestor(tc.input.root, tc.input.p, tc.input.q); output.Val != tc.output {
			t.Errorf("case: %v, output: %v, want: %v", tc.input, output, tc.output)
		}
	}
}
