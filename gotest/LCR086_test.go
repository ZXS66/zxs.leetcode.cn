package gotest

// https://leetcode.cn/problems/M99OJA/description/
import (
	"reflect"
	"testing"
)

func partition(s string) [][]string {
	isPalindrome := func(substr string) bool {
		for i, j := 0, len(substr)-1; i < j; i, j = i+1, j-1 {
			if substr[i] != substr[j] {
				return false
			}
		}
		return true
	}
	var ans [][]string
	n := len(s)
	path := []string{}

	// start 表示当前这段回文子串的开始位置
	var dfs func(int, int)
	dfs = func(i, start int) {
		if i == n {
			ans = append(ans, append([]string(nil), path...)) // 复制 path
			return
		}

		// 不选 i 和 i+1 之间的逗号（i=n-1 时一定要选）
		if i < n-1 {
			dfs(i+1, start)
		}

		// 选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
		if isPalindrome(s[start : i+1]) {
			path = append(path, s[start:i+1])
			dfs(i+1, i+1)             // 下一个子串从 i+1 开始
			path = path[:len(path)-1] // 恢复现场
		}
	}
	dfs(0, 0)
	return ans
}
func TestPartition(t *testing.T) {
	testcases := []LeetcodeTestCase[string, [][]string]{
		{
			input: "google",
			output: [][]string{
				{"goog", "l", "e"}, {"g", "oo", "g", "l", "e"}, {"g", "o", "o", "g", "l", "e"},
			},
		},
		{
			input: "aab",
			output: [][]string{
				{"aa", "b"}, {"a", "a", "b"},
			},
		},
		{
			input: "a",
			output: [][]string{
				{"a"},
			},
		},
	}
	for _, tc := range testcases {
		got := partition(tc.input)
		if !reflect.DeepEqual(tc.output, got) {
			t.Errorf("partition(%v) expected %v, got %v", tc.input, tc.output, got)
		}
	}
}
