package gotest

// 力扣测试用例
type LeetcodeTestCase[IType any, OType any] struct {
	input  IType
	output OType
}

// Definition for a binary tree node
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
