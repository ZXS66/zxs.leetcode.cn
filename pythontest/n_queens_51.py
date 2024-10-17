# https://leetcode.cn/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # 皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子
        columns = set() # 同一列方向
        backslash = set()   # 同一反斜线方向（\），行下标与列下标之差相等
        slash = set()   # 同一斜线方向(/），行下标与列下标之和相等
        ans = []
        # 回溯
        def backtrack(row_idx:int, rows:list[str]) -> None:
            # 一行放置一个皇后
            if row_idx == n:
                ans.append(rows)
                return
            # 尝试在当前行放置皇后
            for col in range(n):
                if col in columns or row_idx - col in backslash or row_idx + col in slash:
                    # 剪枝：皇后不能放在同一列、同一斜线上
                    continue
                new_rows = rows[:] + [ "." * col + "Q" + "." * (n - col - 1)]
                columns.add(col)
                backslash.add(row_idx - col)
                slash.add(row_idx + col)
                backtrack(row_idx + 1, new_rows)
                columns.remove(col) # 回溯
                backslash.remove(row_idx - col) # 回溯
                slash.remove(row_idx + col) # 回溯
        backtrack(0, [])
        return ans
