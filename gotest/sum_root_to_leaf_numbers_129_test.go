package gotest

// https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150

import (
	"math"
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
func sumNumbers(root *TreeNode) int {
	if root == nil {
		return 0
	}
	numbers := numbersOf(root)
	ans := 0
	for _, number := range numbers {
		for _, digit := range number {
			ans += digit
		}
	}
	return ans
}

func numbersOf(root *TreeNode) [][]int {
	if root == nil {
		return nil
	} else if root.Left == nil && root.Right == nil {
		return [][]int{{root.Val}}
	}
	leftDigits, rightDigits := numbersOf(root.Left), numbersOf(root.Right)
	if len(leftDigits) > 0 {
		for i, digits := range leftDigits {
			leftPower := len(leftDigits[i])
			leftDigits[i] = append(digits, root.Val*(int(math.Pow10(leftPower))))
		}
	}
	if len(rightDigits) > 0 {
		for i, digits := range rightDigits {
			rightPower := len(rightDigits[i])
			rightDigits[i] = append(digits, root.Val*(int(math.Pow10(rightPower))))
		}
	}
	return append(leftDigits, rightDigits...)
}

func Test_129(t *testing.T) {
	testcases := []LeetcodeTestCase[*TreeNode, int]{
		{
			input: &TreeNode{
				Val:   1,
				Left:  &TreeNode{Val: 2},
				Right: &TreeNode{Val: 3},
			},
			output: 25,
		},
		{
			input: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   9,
					Left:  &TreeNode{Val: 5},
					Right: &TreeNode{Val: 1},
				},
				Right: &TreeNode{Val: 0},
			},
			output: 1026,
		},
		{
			input: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:  9,
					Left: &TreeNode{Val: 0},
				},
				Right: &TreeNode{Val: 1},
			},
			output: 531,
		},
	}
	for _, tc := range testcases {
		if got := sumNumbers(tc.input); got != tc.output {
			t.Errorf("got %v, want %v", got, tc.output)
		}
	}
}
