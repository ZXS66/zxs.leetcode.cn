# https://leetcode.cn/problems/n-queens-ii/solutions/449388/nhuang-hou-ii-by-leetcode-solution/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def totalNQueens(self, n: int) -> int:
        # 皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子
        columns = set() # 同一列方向
        backslash = set()   # 同一反斜线方向（\），行下标与列下标之差相等
        slash = set()   # 同一斜线方向(/），行下标与列下标之和相等
        # 回溯
        def backtrack(row:int) -> int:
            # 一行放置一个皇后
            if row == n:
                return 1
            # 尝试在当前行放置皇后
            count = 0
            for col in range(n):
                if col in columns or row - col in backslash or row + col in slash:
                    # 剪枝：皇后不能放在同一列、同一斜线上
                    continue
                columns.add(col)
                backslash.add(row - col)
                slash.add(row + col)
                count += backtrack(row + 1)
                columns.remove(col) # 回溯
                backslash.remove(row - col) # 回溯
                slash.remove(row + col) # 回溯
            return count
        return backtrack(0)
