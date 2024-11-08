package gotest

// https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/
import (
	// "math"
	"testing"
)

// 参考链接：https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/solutions/2973328/pan-duan-ju-xing-de-liang-ge-jiao-luo-sh-ug24/
func canReachCorner(xCorner int, yCorner int, circles [][]int) bool {
	// 从 (0,0) 到 (xCorner, yCorner) 是否存在一条路径使得所有圆圈不可重叠
	// 圆圈重叠判断
	// circleOverlapped := func(circleA, circleB []int) bool {
	// 	// \sqrt{(x_1 - x_2)2 + (y_1 - y_2)2}
	// 	distance_square := (circleA[0]-circleB[0])*(circleA[0]-circleB[0]) + (circleA[1]-circleB[1])*(circleA[1]-circleB[1])
	// 	return distance_square <= (circleA[2]+circleB[2])*(circleA[2]+circleB[2])
	// }
	// 判断点是否在圆圈内
	pointInsideCircle := func(circle []int, pointX, pointY int) bool {
		return (circle[0]-pointX)*(circle[0]-pointX)+(circle[1]-pointY)*(circle[1]-pointY) <= circle[2]*circle[2]
	}
	// 求绝对值
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	circleIntersectsTopLeftOfRectangle := func(circle []int, xCorner, yCorner int) bool {
		x, y, r := circle[0], circle[1], circle[2]
		return (abs(x) <= r && 0 <= y && y <= yCorner) ||
			(0 <= x && x <= xCorner && abs(y-yCorner) <= r) ||
			pointInsideCircle([]int{0, yCorner, r}, x, y)
	}
	circleIntersectsBottomRightOfRectangle := func(circle []int, xCorner, yCorner int) bool {
		x, y, r := circle[0], circle[1], circle[2]
		return (abs(y) <= r && 0 <= x && x <= xCorner) ||
			(0 <= y && y <= yCorner && abs(x-xCorner) <= r) ||
			pointInsideCircle([]int{xCorner, 0, r}, x, y)
	}
	circlesIntersectInRectangle := func(circleA, circleB []int, xCorner, yCorner int) bool {
		x1, y1, r1 := circleA[0], circleA[1], circleA[2]
		x2, y2, r2 := circleB[0], circleB[1], circleB[2]
		return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2) <= (r1+r2)*(r1+r2) && x1*r2+x2*r1 < (r1+r2)*xCorner && y1*r2+y2*r1 < (r1+r2)*yCorner
	}
	// 深度优先算法
	searched := make([]bool, len(circles)) // map[圆的索引]是否检索过
	var dfs func(i int) bool
	dfs = func(i int) bool {
		if circleIntersectsBottomRightOfRectangle(circles[i], xCorner, yCorner) {
			return true
		}
		searched[i] = true
		for j := 0; j < len(circles); j++ {
			if !searched[j] && circlesIntersectInRectangle(circles[i], circles[j], xCorner, yCorner) && dfs(j) {
				return true
			}
		}
		return false
	}
	for i := range circles {
		theCircle := circles[i]
		if pointInsideCircle(theCircle, 0, 0) || pointInsideCircle(theCircle, xCorner, yCorner) {
			// 圆包住了原点或者目标点，铁定没有路
			return false
		}
		if !searched[i] && circleIntersectsTopLeftOfRectangle(theCircle, xCorner, yCorner) && dfs(i) {
			return false
		}
	}
	return true // 遍历完所有圆，均未重叠，即可以到达
}

func TestCanReachCorner(t *testing.T) {
	type args struct {
		xCorner int
		yCorner int
		circles [][]int
	}
	testcases := []LeetcodeTestCase[args, bool]{
		{
			input: args{
				xCorner: 3,
				yCorner: 4,
				circles: [][]int{{2, 2, 1}},
			},
			output: true,
		},
		{
			input: args{
				xCorner: 3,
				yCorner: 3,
				circles: [][]int{{1, 1, 2}},
			},
			output: false,
		},
		{
			input: args{
				xCorner: 3,
				yCorner: 3,
				circles: [][]int{{2, 1, 1}, {1, 2, 1}},
			},
			output: false,
		},
		{
			input: args{
				xCorner: 4,
				yCorner: 4,
				circles: [][]int{{5, 5, 1}},
			},
			output: true,
		},
	}
	for _, tc := range testcases {
		got := canReachCorner(tc.input.xCorner, tc.input.yCorner, tc.input.circles)
		if got != tc.output {
			t.Errorf("want %v, got %v", tc.output, got)
		}
	}
}
