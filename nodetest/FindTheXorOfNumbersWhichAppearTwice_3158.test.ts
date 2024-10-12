// https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice/description/

function duplicateNumbersXOR(nums: number[]): number {
    const duplicates: Set<number> = new Set();
    let ans = 0;
    for (const num of nums) {
        // 数组中的数字 要么 出现一次，要么 出现两次。
        if (duplicates.has(num)) {
            ans ^= num;
        } else {
            duplicates.add(num);
        }
    }
    return duplicates.size ? ans : 0;
};



// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [1, 2, 1, 3], result: 1 },
    { nums: [1, 2, 3], result: 0 },
    { nums: [1, 2, 2, 1], result: 3 },
];

describe.each(testcases)(`nums: $nums`, ({ nums, result }) => {
    test(`returns ${result}`, () => {
        expect(duplicateNumbersXOR(nums)).toBe(result);
    });
});
