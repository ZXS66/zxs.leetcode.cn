# https://www.nowcoder.com/practice/56e54f4c2e3c4a58abfe76dbc1da1d7e?channelPut=w251acm
#

from typing import Literal

def prevent_flood(x: int, y: int, matrix: list[list[str]]) -> int:
    # x == len(matrix) and y == len(matrix[0])
    # matrix should be type of list[list[Literal['*','0']]]

    # inititial the steps
    steps: list[tuple[int, int]] = []
    for i in range(max(x, y)):
        if i < y:
            if matrix[0][i] == '0':
                steps.append((0, i))
            if matrix[x - 1][i] == '0':
                steps.append((x - 1, i))
        if i < x:
            if matrix[i][0] == '0':
                steps.append((i, 0))
            if matrix[i][y - 1] == '0':
                steps.append((i, y - 1))

    while steps:
        i, j = steps.pop(0)
        if matrix[i][j] == '0':
            matrix[i][j] = '*'
            if i > 0 and matrix[i - 1][j] == '0':
                steps.append((i - 1, j))
            if i < x - 1 and matrix[i + 1][j] == '0':
                steps.append((i + 1, j))
            if j > 0 and matrix[i][j - 1] == '0':
                steps.append((i, j - 1))
            if j < y - 1 and matrix[i][j + 1] == '0':
                steps.append((i, j + 1))

    # count remaining zeros
    result = 0
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == '0':
                result += 1

    return result
