package gotest

import (
	"sort"
	"testing"
)

// https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150

func kSmallestPairs(nums1 []int, nums2 []int, k int) (ans [][]int) {
	m, n := len(nums1), len(nums2)

	// 二分查找第 k 小的数对和
	left, right := nums1[0]+nums2[0], nums1[m-1]+nums2[n-1]+1
	pairSum := left + sort.Search(right-left, func(sum int) bool {
		sum += left
		cnt := 0
		i, j := 0, n-1
		for i < m && j >= 0 {
			if nums1[i]+nums2[j] > sum {
				j--
			} else {
				cnt += j + 1
				i++
			}
		}
		return cnt >= k
	})

	// 找数对和小于 pairSum 的数对
	i := n - 1
	for _, num1 := range nums1 {
		for i >= 0 && num1+nums2[i] >= pairSum {
			i--
		}
		for _, num2 := range nums2[:i+1] {
			ans = append(ans, []int{num1, num2})
			if len(ans) == k {
				return
			}
		}
	}

	// 找数对和等于 pairSum 的数对
	i = n - 1
	for _, num1 := range nums1 {
		for i >= 0 && num1+nums2[i] > pairSum {
			i--
		}
		for j := i; j >= 0 && num1+nums2[j] == pairSum; j-- {
			ans = append(ans, []int{num1, nums2[j]})
			if len(ans) == k {
				return
			}
		}
	}
	return

	// 作者：力扣官方题解
	// 链接：https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/solutions/1208350/cha-zhao-he-zui-xiao-de-kdui-shu-zi-by-l-z526/
	// 来源：力扣（LeetCode）
	// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}

func Test_Q373(t *testing.T) {
	type args = struct {
		nums1 []int
		nums2 []int
		k     int
	}
	type ret = [][]int

	testcases := []LeetcodeTestCase[args, ret]{
		{
			input: args{
				nums1: []int{1, 7, 11},
				nums2: []int{2, 4, 6},
				k:     3,
			},
			output: ret{{1, 2}, {1, 4}, {1, 6}},
		},
		{
			input: args{
				nums1: []int{1, 1, 2},
				nums2: []int{1, 2, 3},
				k:     2,
			},
			output: ret{{1, 1}, {1, 1}},
		},
	}
	for _, tc := range testcases {
		got := kSmallestPairs(tc.input.nums1, tc.input.nums2, tc.input.k)
		// check returned value length
		if len(got) != len(tc.output) || len(got) != tc.input.k {
			t.Errorf("got: %v, want: %v", got, tc.output)
		}
		// sample test sum
		got2 := got[tc.input.k-1][0] + got[tc.input.k-1][1]
		output2 := tc.output[tc.input.k-1][0] + tc.output[tc.input.k-1][1]
		if got2 != output2 {
			t.Errorf("got: %v, want: %v", got2, output2)
		}
	}
}
