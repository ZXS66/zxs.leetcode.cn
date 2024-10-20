# https://leetcode.cn/problems/construct-quad-tree/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        return self.construct_helper(grid, 0, 0, len(grid))

    def construct_helper(
        self, grid: list[list[int]], row: int, col: int, size: int
    ) -> Node:
        if size == 1:
            return Node(grid[row][col], True, None, None, None, None)

        # 检查网格中的所有值是否相同
        val = grid[row][col]
        equality = all(
            [grid[row + i][col + j] == val for i in range(size) for j in range(size)]
        )
        if equality:
            return Node(val, True, None, None, None, None)

        # 当前网格的值不同
        mid = size // 2
        topLeft = self.construct_helper(grid, row, col, mid)
        topRight = self.construct_helper(grid, row, col + mid, mid)
        bottomLeft = self.construct_helper(grid, row + mid, col, mid)
        bottomRight = self.construct_helper(grid, row + mid, col + mid, mid)
        # 将 isLeaf 设为 False， 将 val 设为任意值
        return Node(
            True,
            False,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight,
        )
