/**
 * @param {number[]} nums asc numbers
 * @return {number}
 */
var removeDuplicates = function (nums) {
    const n = nums.length;
    if (n <= 2) {
        return n;
    }
    let slow = 2, fast = 2;
    while (fast < n) {
        if (nums[slow - 2] != nums[fast]) {
            nums[slow] = nums[fast];
            ++slow;
        }
        ++fast;
    }
    return slow;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [1, 1, 1, 2, 2, 3], k: 5 },
    { nums: [0, 0, 1, 1, 1, 1, 2, 3, 3], k: 7 },
    { nums: [1, 1, 1], k: 2 },
];

describe.each(testcases)(`nums: $nums, k: $k`, ({ nums, k }) => {
    test(`returns`, () => {
        expect(removeDuplicates(nums)).toBe(k);
    });
});
