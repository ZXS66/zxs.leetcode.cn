// https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/description/

function minCost(maxTime: number, edges: number[][], passingFees: number[]): number {
    const n = passingFees.length;
    const fee: number[][] = Array.from({ length: maxTime + 1 }, () => new Array(n).fill(Infinity)); // fee[i][j] 表示在时间 i 时，从城市 0 到城市 j 的最小花费
    fee[0][0] = passingFees[0]; // 起始位置也要付费
    for (let t = 1; t <= maxTime; t++) {
        for (const [x, y, tm] of edges) {
            if (tm <= t) {
                fee[t][x] = Math.min(fee[t][x], fee[t - tm][y] + passingFees[x]);
                fee[t][y] = Math.min(fee[t][y], fee[t - tm][x] + passingFees[y]);
            }
        }
    }
    let ans = Infinity;
    for (let i = 1; i <= maxTime; ++i) {
        ans = Math.min(ans, fee[i][n - 1]);
    }
    return ans === Infinity ? -1 : ans;
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { maxTime: 30, edges: [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], passingFees: [5, 1, 2, 20, 20, 3], result: 11 },
    { maxTime: 29, edges: [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], passingFees: [5, 1, 2, 20, 20, 3], result: 48 },
    { maxTime: 25, edges: [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], passingFees: [5, 1, 2, 20, 20, 3], result: -1 },
];

describe.each(testcases)(`maxTime: $maxTime, edge: $edge, passingFees: $passingFees`, ({ maxTime, edges, passingFees, result }) => {
    test(`returns ${result}`, () => {
        expect(minCost(maxTime, edges, passingFees)).toBe(result);
    });
});

