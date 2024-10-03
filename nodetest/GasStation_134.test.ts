// https://leetcode.cn/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

function canCompleteCircuit(gas: number[], cost: number[]): number {
    const n = gas.length;
    let i = 0;
    while (i < n) {
        if (gas[i] < cost[i]) {
            i++;
            continue;
        }
        let balance = 0;
        let move = 0;
        while (move < n) {
            const j = (i + move) % n;
            balance += (gas[j] - cost[j]);
            if (balance < 0) {
                break;
            }
            move++;
        }
        if (move === n) {
            return i;
        }
        else {
            // 贪心，直接跨到上次循环最后有结余油量的站点
            i += (move + 1);
        }
    }
    return -1;
};
// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { gas: [1, 2, 3, 4, 5], cost: [3, 4, 5, 1, 2], result: 3 },
    { gas: [2, 3, 4], cost: [3, 4, 3], result: -1 },
];

describe.each(testcases)(`gas: $gas, cost: $cost`, ({ gas, cost, result }) => {
    test(`returns ${result}`, () => {
        expect(canCompleteCircuit(gas, cost)).toBe(result);
    });
});

