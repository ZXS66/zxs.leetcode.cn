package gotest

// https://leetcode.cn/problems/design-neighbor-sum-service/description/
import "testing"

type NeighborSum struct {
	grid [][]int
}

func NeighborSumConstructor(grid [][]int) NeighborSum {
	return NeighborSum{grid: grid}
}

func (this *NeighborSum) AdjacentSum(value int) int {
	// step 1: find the position of the value
	top, right, bottom, left := 0, 0, 0, 0
	for i, row := range this.grid {
		for j, v := range row {
			if v == value {
				// step 2: find the adjacent values
				if i > 0 {
					top = this.grid[i-1][j]
				}
				if j < len(row)-1 {
					right = row[j+1]
				}
				if i < len(this.grid)-1 {
					bottom = this.grid[i+1][j]
				}
				if j > 0 {
					left = row[j-1]
				}
				break
			}
		}
		if top != 0 || right != 0 || bottom != 0 || left != 0 {
			break
		}
	}
	// step 3: calculate sum
	return top + right + bottom + left
}

func (this *NeighborSum) DiagonalSum(value int) int {
	// step 1: find the position of the value
	leftTop, rightTop, rightBottom, leftBottom := 0, 0, 0, 0
	for i, row := range this.grid {
		for j, v := range row {
			if v == value {
				// step 2: find the diagonal values
				if i > 0 && j > 0 {
					leftTop = this.grid[i-1][j-1]
				}
				if i > 0 && j < len(row)-1 {
					rightTop = this.grid[i-1][j+1]
				}
				if i < len(this.grid)-1 && j < len(row)-1 {
					rightBottom = this.grid[i+1][j+1]
				}
				if i < len(this.grid)-1 && j > 0 {
					leftBottom = this.grid[i+1][j-1]
				}
				break
			}
		}
		if leftTop != 0 || rightTop != 0 || rightBottom != 0 || leftBottom != 0 {
			break
		}
	}
	// step 3: calculate sum
	return leftTop + rightTop + rightBottom + leftBottom
}

func TestNeighborSum(t *testing.T) {
	ns1 := NeighborSumConstructor([][]int{{0, 1, 2}, {3, 4, 5}, {6, 7, 8}})
	if got1 := ns1.AdjacentSum(1); got1 != 6 {
		t.Errorf("want %v, got %v", 6, got1)
	}
	if got2 := ns1.AdjacentSum(4); got2 != 16 {
		t.Errorf("want %v, got %v", 16, got2)
	}
	if got3 := ns1.DiagonalSum(4); got3 != 16 {
		t.Errorf("want %v, got %v", 16, got3)
	}
	if got4 := ns1.DiagonalSum(8); got4 != 4 {
		t.Errorf("want %v, got %v", 4, got4)
	}
	ns2 := NeighborSumConstructor([][]int{{1, 2, 0, 3}, {4, 7, 15, 6}, {8, 9, 10, 11}, {12, 13, 14, 5}})
	if got5 := ns2.AdjacentSum(15); got5 != 23 {
		t.Errorf("want %v, got %v", 23, got5)
	}
	if got6 := ns2.DiagonalSum(9); got6 != 45 {
		t.Errorf("want %v, got %v", 45, got6)
	}
}
