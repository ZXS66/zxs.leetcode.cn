// https://leetcode.cn/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

function isValidSudoku(board: string[][]): boolean {
    for (let i = 0; i < 9; i++) {
        const row = board[i];
        if (!check(row)) {
            return false;
        }
        const col: string[] = [];
        const box: string[] = [];
        for (let j = 0; j < 9; j++) {
            col.push(board[j][i]);
            box.push(board[Math.floor(i / 3) * 3 + Math.floor(j / 3)][j % 3 + 3 * Math.floor(i % 3)]);
        }
        if (!check(col) || !check(box)) {
            return false;
        }
    }
    return true;
};
function check(item: string[]): boolean {
    const set = new Set<string>();
    for (let i = 0; i < 9; i++) {
        const num = item[i];
        if (num !== ".") {
            if (set.has(num)) {
                return false;
            }
            set.add(num);
        }
    }
    return true;
}

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        board: [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ], result: true
    },
    {
        board: [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ], result: false
    }
];

describe.each(testcases)(`board:$board`, ({ board, result }) => {
    test(`returns ${result}`, () => {
        expect(isValidSudoku(board)).toBe(result);
    });
});
