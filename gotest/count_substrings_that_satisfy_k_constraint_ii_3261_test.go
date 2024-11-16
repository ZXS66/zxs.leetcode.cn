package gotest

// https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/

import (
	"reflect"
	"testing"
)

func countKConstraintSubstringsII(s string, k int, queries [][]int) []int64 {
	// satisfyKConstraint := func(substr string) bool {
	// 	zeroCount, oneCount := 0, 0
	// 	for _, ch := range substr {
	// 		if ch == '0' {
	// 			zeroCount++
	// 			if zeroCount > k && oneCount > k {
	// 				return false
	// 			}
	// 		} else {
	// 			oneCount++
	// 			if oneCount > k && zeroCount > k {
	// 				return false
	// 			}
	// 		}
	// 	}
	// 	return true
	// }
	// cache := make(map[string]int64)
	// countSatisfy := func(substr string) int64 {
	// 	cacheValue, ok := cache[substr]
	// 	if ok {
	// 		return cacheValue
	// 	}
	// 	res := int64(0)
	// 	n := len(substr)
	// 	for subStrLen := 1; subStrLen < n+1; subStrLen++ {
	// 		for i := 0; i < n-subStrLen+1; i++ {
	// 			if satisfyKConstraint(substr[i : i+subStrLen]) {
	// 				res++
	// 			}
	// 		}
	// 	}
	// 	cache[substr] = res
	// 	return res
	// }
	// res := make([]int64, len(queries))
	// for i, query := range queries {
	// 	res[i] = countSatisfy(s[query[0] : query[1]+1])
	// }
	// return res

	// 链接：https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/solutions/2884463/hua-dong-chuang-kou-qian-zhui-he-er-fen-jzo25/
	n := len(s)
	left := make([]int, n)
	sum := make([]int, n+1)
	cnt := [2]int{}
	l := 0
	for i, c := range s {
		cnt[c&1]++
		for cnt[0] > k && cnt[1] > k {
			cnt[s[l]&1]--
			l++
		}
		left[i] = l
		sum[i+1] = sum[i] + i - l + 1
	}

	right := make([]int, n)
	l = 0
	for i := range right {
		for l < n && left[l] < i {
			l++
		}
		right[i] = l
	}

	ans := make([]int64, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]
		j := min(right[l], r+1)
		ans[i] = int64(sum[r+1] - sum[j] + (j-l+1)*(j-l)/2)
	}
	return ans

}

func TestCountKConstraintSubstringsII(t *testing.T) {
	type args struct {
		s       string
		k       int
		queries [][]int
	}
	testcases := []LeetcodeTestCase[args, []int64]{
		{
			input: args{
				s:       "0001111",
				k:       2,
				queries: [][]int{{0, 6}},
			},
			output: []int64{26},
		},
		{
			input: args{
				s:       "010101",
				k:       1,
				queries: [][]int{{0, 5}, {1, 4}, {2, 3}},
			},
			output: []int64{15, 9, 3},
		},
	}
	for _, tc := range testcases {
		got := countKConstraintSubstringsII(tc.input.s, tc.input.k, tc.input.queries)
		if !reflect.DeepEqual(got, tc.output) {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
