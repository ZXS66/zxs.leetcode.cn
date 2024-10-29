package gotest

// https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/description/
import (
	"reflect"
	"testing"
)

func validStrings(n int) []string {
	if n == 1 {
		return []string{"0", "1"}
	}
	tmp := validStrings(n - 1)
	ans := make([]string, 0)
	for _, v := range tmp {
		if v[len(v)-1] == '0' {
			ans = append(ans, v+"1")
		} else {
			ans = append(ans, v+"0", v+"1")
		}
	}
	return ans
}

func Test_validStrings(t *testing.T) {
	testcases := []LeetcodeTestCase[int, []string]{
		{
			input:  3,
			output: []string{"010", "011", "101", "110", "111"},
		},
		{
			input:  1,
			output: []string{"0", "1"},
		},
	}
	for _, tc := range testcases {
		if got := validStrings(tc.input); !reflect.DeepEqual(got, tc.output) {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
