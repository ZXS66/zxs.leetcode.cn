// https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

function maxProfit(prices: number[]): number {
    let profit = 0;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];
        }
    }
    return profit;
};

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    { prices: [7, 1, 5, 3, 6, 4], result: 7 },
    { prices: [1, 2, 3, 4, 5], result: 4 },
    { prices: [7, 6, 4, 3, 1], result: 0 },
];

describe.each(testcases)(`prices: $prices, result: $result`, ({ prices, result }) => {
    test(`returns`, () => {
        expect(maxProfit(prices)).toBe(result);
    });
});


