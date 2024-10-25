package gotest

import (
	"fmt"
	"testing"
)

func TestAppendSlice(t *testing.T) {
	s1 := []int{1, 2, 3}
	idx := 1
	// s2:= append(s1[:idx], s1[idx+1:]...)	// this is wrong as the append function will modify underlying slice (first argument) due to reallocation
	s2 := append(make([]int, 0), s1[:idx]...)
	s2 = append(s2, s1[idx+1:]...)
	if len(s2) != 2 {
		t.Fatal("s2 should have length 2")
	}
	if len(s1) != 3 || s1[0] != 1 || s1[1] != 2 || s1[2] != 3 {
		fmt.Println(s1)
		t.Fatal("s1 should be [1,2,3]")
	}
}
