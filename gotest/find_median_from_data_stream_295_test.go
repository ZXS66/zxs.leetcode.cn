package gotest

// https://leetcode.cn/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150
import (
	"slices"
	"testing"
)

type MedianFinder struct {
	data []int
}

func MedianFinderConstructor() MedianFinder {
	return MedianFinder{}
}

func (mfinder *MedianFinder) AddNum(num int) {
	mfinder.data = append(mfinder.data, num)
}

func (mfinder *MedianFinder) FindMedian() float64 {
	slices.Sort(mfinder.data)
	n := len(mfinder.data)
	if n%2 == 0 {
		return float64(mfinder.data[n/2]+mfinder.data[n/2-1]) / 2
	} else {
		return float64(mfinder.data[n/2])
	}
}

func TestMedianFinder(t *testing.T) {
	obj := MedianFinderConstructor()
	obj.AddNum(1)
	obj.AddNum(2)
	if got1 := obj.FindMedian(); got1 != 1.5 {
		t.Errorf("want %v, got %v", 1.5, got1)
	}
	obj.AddNum(3)
	if got2 := obj.FindMedian(); got2 != 2.0 {
		t.Errorf("want %v, got %v", 2, got2)
	}
}
