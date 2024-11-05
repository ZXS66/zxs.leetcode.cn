package gotest

// https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/description/
import (
	"strconv"
	"testing"
)

func minChanges(n int, k int) int {
	if n == k {
		return 0
	}
	str1, str2 := strconv.FormatInt(int64(n), 2), strconv.FormatInt(int64(k), 2)
	if len(str1) < len(str2) {
		// 任意一个值为 1 的位，并将其改为 0
		// 不能反向更改
		return -1
	}
	paddingLeft := len(str1) - len(str2)
	ans := 0
	for i := 0; i < len(str1); i++ {
		if i < paddingLeft {
			// 填充 0
			if str1[i] == '1' {
				ans++
			}
			continue
		}
		a, b := str1[i], str2[i-paddingLeft]
		if a == b {
			continue
		}
		if a == '0' {
			return -1
		}
		ans++
	}
	return ans
}
func TestMinChange(t *testing.T) {
	type args struct {
		n int
		k int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input:  args{n: 13, k: 4},
			output: 2,
		},
		{
			input:  args{n: 21, k: 21},
			output: 0,
		},
		{
			input:  args{n: 14, k: 13},
			output: -1,
		},
		{
			input:  args{n: 54, k: 4},
			output: 3,
		},
	}
	for _, tc := range testcases {
		got := minChanges(tc.input.n, tc.input.k)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
