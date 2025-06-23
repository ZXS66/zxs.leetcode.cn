// https://leetcode.cn/problems/next-permutation/?envType=study-plan-v2&envId=top-100-liked

/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    function swap(i:number, j:number) {
        const temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    let i = nums.length - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }
    if (i >= 0) {
        let j = nums.length - 1;
        while (j >= 0 && nums[i] >= nums[j]) {
            j -= 1;
        }
        swap(i, j);
    }
    let left = i + 1, right = nums.length - 1;
    while (left < right) {
        swap(left, right);
        left++;
        right--;
    }
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [1, 2, 3], result: [1, 3, 2] },
    { nums: [3, 2, 1], result: [1, 2, 3] },
    { nums: [1, 1, 5], result: [1, 5, 1] },
];

describe.each(testcases)(`nums: $nums, result: $result`, ({ nums, result }) => {
    test(`returns ${result}`, () => {
        nextPermutation(nums);
        expect(JSON.stringify(nums)).toBe(JSON.stringify(result));
    });
});
