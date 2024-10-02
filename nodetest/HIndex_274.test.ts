// https://leetcode.cn/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

function hIndex(citations: number[]): number {
    citations.sort((a, b) => b - a);
    let i = 0;
    while (i < citations.length && citations[i] > i) {
        i++;
    }
    return i;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { citations: [3, 0, 6, 1, 5], result: 3 },
    { citations: [1, 3, 1], result: 1 },
];

describe.each(testcases)(`citations : $citations `, ({ citations, result }) => {
    test(`returns ${result}`, () => {
        expect(hIndex(citations)).toBe(result);
    });
});
