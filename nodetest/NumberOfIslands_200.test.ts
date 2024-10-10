// https://leetcode.cn/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

function numIslands(grid: string[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let ans = 0;
    const dfs = (i: number, j: number) => {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] === '0') return;
        grid[i][j] = '0';
        dfs(i - 1, j);
        dfs(i + 1, j);
        dfs(i, j - 1);
        dfs(i, j + 1);
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === '1') {
                ans++;
                dfs(i, j);
            }
        }
    }
    return ans;
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    {
        grid: [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ], result: 1
    },
    {
        grid: [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ], result: 3
    },
];

describe.each(testcases)(`grid: $grid`, ({ grid, result }) => {
    test(`returns ${result}`, () => {
        expect(numIslands(grid)).toBe(result);
    });
});


