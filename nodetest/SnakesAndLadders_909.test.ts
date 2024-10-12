// https://leetcode.cn/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150

function snakesAndLadders(board: number[][]): number {
    const n = board.length; // n == board.length == board[i].length
    // build the graph via board
    const goto = new Map<number, number>();
    for (let i = 1; i <= n * n; i++) {
        // 方格按从 1 到 n^2 编号，编号遵循 转行交替方式 ，从左下角开始 （即，从 board[n - 1][0] 开始）的每一行改变方向。
        const r = Math.floor((i - 1) / n);
        const c = r % 2 ? (n - 1 - (i - 1) % n) : ((i - 1) % n);
        const target = board[n - 1 - r][c];
        if (target > 0) {
            goto.set(i, target);
        }
    }

    const queue: number[][] = [];    // [[index, moves]]
    const visited = new Set<number>();  // index of moved steps
    queue.push([1, 0]);
    while (queue.length) {
        const [cur, moves] = queue.shift()!;
        for (let i = 1; i <= 6; i++) {
            let next = cur + i;
            if (next > n * n) {
                break;
            }
            if (goto.has(next)) {
                next = goto.get(next)!;
            }
            if (next === n * n) {
                return moves + 1;
            }
            if (!visited.has(next)) {
                visited.add(next);
                queue.push([next, moves + 1]);
            }
        }
    }
    return -1;
};

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        board: [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]],
        result: 4
    },
    {
        board: [[-1, -1], [-1, 3]],
        result: 1
    }
];

describe.each(testcases)(`matrix:$matrix`, ({ board, result }) => {
    test(`returns ${result}`, () => {
        expect(snakesAndLadders(board)).toBe(result);
    });
});
