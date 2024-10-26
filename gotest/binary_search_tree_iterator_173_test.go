package gotest

// https://leetcode.cn/problems/binary-search-tree-iterator/description/?envType=study-plan-v2&envId=top-interview-150

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
type BSTIterator struct {
	stack []*TreeNode
	cur   *TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
	return BSTIterator{cur: root}
}

func (it *BSTIterator) Next() int {
	for node := it.cur; node != nil; node = node.Left {
		it.stack = append(it.stack, node)
	}
	it.cur, it.stack = it.stack[len(it.stack)-1], it.stack[:len(it.stack)-1]
	val := it.cur.Val
	it.cur = it.cur.Right
	return val
}

func (it *BSTIterator) HasNext() bool {
	return it.cur != nil || len(it.stack) > 0
}

// 链接：https://leetcode.cn/problems/binary-search-tree-iterator/solutions/683126/er-cha-sou-suo-shu-die-dai-qi-by-leetcod-4y0y/

func Test_173(t *testing.T) {
	root := &TreeNode{
		Val:  7,
		Left: &TreeNode{Val: 3},
		Right: &TreeNode{
			Val:   15,
			Left:  &TreeNode{Val: 9},
			Right: &TreeNode{Val: 20},
		},
	}
	// bSTIterator := Constructor(root)
	bSTIterator := Constructor(root)
	if output1 := bSTIterator.Next(); output1 != 3 {
		t.Error("Test = ", output1, "But Excepted = ", 3)
	}
	if output2 := bSTIterator.Next(); output2 != 7 {
		t.Error("Test = ", output2, "But Excepted = ", 7)
	}
	if output3 := bSTIterator.HasNext(); !output3 {
		t.Error("Test = ", output3, "But Excepted = ", true)
	}
	if output4 := bSTIterator.Next(); output4 != 9 {
		t.Error("Test = ", output4, "But Excepted = ", 9)
	}
	if output5 := bSTIterator.HasNext(); !output5 {
		t.Error("Test = ", output5, "But Excepted = ", true)
	}
	if output6 := bSTIterator.Next(); output6 != 15 {
		t.Error("Test = ", output6, "But Excepted = ", 15)
	}
	if output7 := bSTIterator.HasNext(); !output7 {
		t.Error("Test = ", output7, "But Excepted = ", true)
	}
	if output8 := bSTIterator.Next(); output8 != 20 {
		t.Error("Test = ", output8, "But Excepted = ", 20)
	}
	if output9 := bSTIterator.HasNext(); output9 {
		t.Error("Test = ", output9, "But Excepted = ", false)
	}
}
