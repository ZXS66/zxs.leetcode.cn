// https://leetcode.cn/problems/minimum-cost-for-tickets/

function mincostTickets(days: number[], costs: number[]): number {
    if (days.length === 1) {
        return Math.min(...costs);
    }
    const calendar = new Set(days);
    const memo: Map<number, number> = new Map();
    const dp = (i: number): number => {
        if (i > 365) return 0;
        if (memo.has(i)) {
            return memo.get(i) as number;
        }
        if (calendar.has(i)) {
            // 要出行，得规划事件、金额、感情等等等
            memo.set(i, Math.min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2]));
        } else {
            // 不必出行，嘿嘿
            memo.set(i, dp(i + 1));
        }
        return memo.get(i) as number;
    }
    return dp(1);
};
// https://leetcode.cn/problems/minimum-cost-for-tickets/solutions/233810/zui-di-piao-jie-by-leetcode-solution/

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    { days: [1, 4, 6, 7, 8, 20], costs: [2, 7, 15], result: 11 },
    { days: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs: [2, 7, 15], result: 17 },
    { days: [364], costs: [3, 3, 1], result: 1 },
];

describe.each(testcases)(`days: $days, costs: $costs`, ({ days, costs, result }) => {
    test(`returns ${result}`, () => {
        expect(mincostTickets(days, costs)).toBe(result);
    });
});

