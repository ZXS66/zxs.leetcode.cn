// https://leetcode.cn/problems/minimum-number-of-refueling-stops/description/

/**
 * @param target 目的地位于出发位置东面 target 英里处
 * @param startFuel 最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油
 * @param stations stations[i] = [positioni, fueli], 表示第 i 个加油站位于出发位置东面 positioni 英里处，并且有 fueli 升汽油
 * @returns 汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 
 */
function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
    if (startFuel >= target) return 0;
    const n = stations.length;
    if (n === 0) return startFuel >= target ? 0 : -1;

    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = startFuel;
    for (let i = 0; i < n; i++) {
        for (let j = n; j >= 0; j--) { // 从后往前遍历
            if (dp[j] >= stations[i][0]) {
                dp[j + 1] = Math.max(dp[j + 1], dp[j] + stations[i][1]);
            }
        }
    }

    for (let i = 0; i <= n; i++) {
        if (dp[i] >= target) {
            return i;
        }
    }
    return -1;
};



// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { target: 1, startFuel: 1, stations: [], result: 0 },
    { target: 100, startFuel: 1, stations: [[10, 100]], result: -1 },
    { target: 100, startFuel: 10, stations: [[10, 60], [20, 30], [30, 30], [60, 40]], result: 2 },
    { target: 100, startFuel: 50, stations: [[25,25],[50,50]], result: 1 },
];

describe.each(testcases)(`target: $target, startFuel: $startFuel`, ({ target, startFuel, stations, result }) => {
    test(`returns ${result}`, () => {
        expect(minRefuelStops(target, startFuel, stations)).toBe(result);
    });
});

