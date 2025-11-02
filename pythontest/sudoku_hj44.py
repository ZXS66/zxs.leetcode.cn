# https://www.nowcoder.com/practice/78a1a4ebe8a34c93aac006c44f6bf8a1?tpId=37&tqId=21267&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

class Solution:
    def resolve_sudoku(self, matrix:list[list[int]]) -> list[list[int]]:
        def is_valid(matrix, row, col, num):
            for i in range(9):
                if matrix[row][i] == num or matrix[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if matrix[i][j] == num:
                        return False
            return True

        def solve(matrix):
            for i in range(9):
                for j in range(9):
                    if matrix[i][j] == 0:
                        for num in range(1, 10):
                            if is_valid(matrix, i, j, num):
                                matrix[i][j] = num
                                if solve(matrix):
                                    return True
                                matrix[i][j] = 0
                        return False
            return True

        solve(matrix)
        return matrix
