package gotest

// https://leetcode.cn/problems/ipo/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"container/heap"
	"reflect"
	"sort"
	"testing"
)

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	// n == profits.length, n == capital.length, 1 <= n <= 105
	n := len(profits)
	type pair struct{ c, p int }
	arr := make([]pair, n)
	for i, p := range profits {
		arr[i] = pair{capital[i], p}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].c < arr[j].c })

	h := &hp{}
	for cur := 0; k > 0; k-- {
		for cur < n && arr[cur].c <= w {
			heap.Push(h, arr[cur].p)
			cur++
		}
		if h.Len() == 0 {
			break
		}
		w += heap.Pop(h).(int)
	}
	return w
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}

// 链接：https://leetcode.cn/problems/ipo/solutions/984750/ipo-by-leetcode-solution-89zm/

func TestFindMaximizedCapital(t *testing.T) {
	type args struct {
		k       int
		w       int
		profits []int
		capital []int
	}
	testcases := []LeetcodeTestCase[args, int]{
		{
			input: args{
				k:       2,
				w:       0,
				profits: []int{1, 2, 3},
				capital: []int{0, 1, 1},
			},
			output: 4,
		},
		{
			input: args{
				k:       3,
				w:       0,
				profits: []int{1, 2, 3},
				capital: []int{0, 1, 2},
			},
			output: 6,
		},
	}
	for _, tc := range testcases {
		got := findMaximizedCapital(tc.input.k, tc.input.w, tc.input.profits, tc.input.capital)
		if !reflect.DeepEqual(got, tc.output) {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
