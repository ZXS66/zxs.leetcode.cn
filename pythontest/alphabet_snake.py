def snake_move(
    steps: int, alphabet: list[str], row: int, col: int, matrix: list[list[str]]
) -> list[list[int]]:
    def dfs(
        matrix: list[list[str]], x: int, y: int, move: list[list[int]]
    ) -> tuple[bool, list[list[int]]]:
        # x: current x-coordinate
        # y: current y-coordinate
        # move: current move count (should be less than steps)
        if len(move) == steps:
            return True, move
        count = len(move)
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0:
                nx += row
            elif nx >= row:
                nx -= row
            if ny < 0:
                ny += col
            elif ny >= col:
                ny -= col
            if matrix[nx][ny] == alphabet[count]:
                prev = matrix[nx][ny]
                matrix[nx][ny] = "*"  # 好马不吃回头草
                move.append([nx, ny])
                flag, move = dfs(matrix, nx, ny, move)
                if flag:
                    return True, move
                # 回溯
                matrix[nx][ny] = prev
                move.pop()
        return False, move

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == alphabet[0]:
                matrix[i][j] = "*"
                flag, move = dfs(matrix, i, j, [[i, j]])
                if flag:
                    return move
                matrix[i][j] = alphabet[0]

    return [[-1, -1]]
