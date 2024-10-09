# https://leetcode.cn/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                cnt = self.alive_neighbors(i, j)
                if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                    # 1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
                    # 3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
                    board[i][j] = 3
                if board[i][j] == 0 and cnt == 3:
                    # 4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
                    board[i][j] = 2
        for i in range(self.m):
            for j in range(self.n):
                # if board[i][j] & 1:
                #     board[i][j] = 1
                # else:
                #     board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

    def alive_neighbors(self, i, j):
        cnt = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x == i and y == j:
                    continue
                if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] & 1:
                    cnt += 1
        return cnt
