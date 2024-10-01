// https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

function canJump(nums: number[]): boolean {
    const n = nums.length;
    let rightMost = 0;
    for (let i = 0; i < n; i++) {
        if (i <= rightMost) {
            rightMost = Math.max(rightMost, i + nums[i]);
            if (rightMost >= n - 1) {
                return true;
            }
        }
    }
    return false;
};


// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    { nums: [2, 3, 1, 1, 4], result: true },
    { nums: [3, 2, 1, 0, 4], result: false },
];

describe.each(testcases)(`nums: $nums, result: $result`, ({ nums, result }) => {
    test(`returns`, () => {
        expect(canJump(nums)).toBe(result);
    });
});

