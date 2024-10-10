// https://leetcode.cn/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150

/**
 Do not return anything, modify board in-place instead.
 */
function solve(board: string[][]): void {
    const m = board.length;
    const n = board[0].length;
    const visited = new Array(m).fill(0).map(() => new Array(n).fill(false));
    const dfs = (i: number, j: number) => {
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || board[i][j] === 'X') {
            return;
        }
        visited[i][j] = true;
        dfs(i - 1, j);
        dfs(i + 1, j);
        dfs(i, j - 1);
        dfs(i, j + 1);
    }
    for (let i = 0; i < m; i++) {
        dfs(i, 0);
        dfs(i, n - 1);
    }
    for (let j = 0; j < n; j++) {
        dfs(0, j);
        dfs(m - 1, j);
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (!visited[i][j] && board[i][j] === 'O') {
                board[i][j] = 'X';
            }
        }
    }
};

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        board: [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
        result: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    },
    {
        board: [["X"]],
        result: [["X"]]
    }
];

describe.each(testcases)(`board:$board`, ({ board, result }) => {
    test(`returns ${result}`, () => {
        solve(board);
        expect(JSON.stringify(board)).toEqual(JSON.stringify(result));
    });
});
