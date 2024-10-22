package gotest

// type LeetcodeTestCase struct {
// 	input  interface{}
// 	output interface{}
// }

type LeetcodeTestCase[IType any, OType any] struct {
	input  IType
	output OType
}
