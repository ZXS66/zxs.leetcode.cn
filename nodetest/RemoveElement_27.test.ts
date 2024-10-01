function removeElement(nums: number[], val: number): number {
    let len = nums.length;
    let k = 0;
    for (let i = 0; i < len; i++) {
        if (nums[i] === val) {
            nums[i] = 0;
        } else {
            k++;
        }
    }
    nums.sort((a, b) => b - a);
    return k;
};

// test cases
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [3, 2, 2, 3], val: 3, result: 2 },
    { nums: [0, 1, 2, 2, 3, 0, 4, 2], val: 2, result: 5 },
];

describe.each(testcases)(`nums: $nums, val: $val`, ({ nums, val, result }) => {
    test(`returns ${result}`, () => {
        expect(removeElement(nums, val)).toBe(result);
    });
});
