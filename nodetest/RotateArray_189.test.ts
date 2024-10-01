// https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

/**
 Do not return anything, modify nums in-place instead.
 */
 function rotate(nums: number[], k: number): void {
    k = k % nums.length;
    // nums = nums.slice(nums.length - k).concat(nums.slice(0, nums.length - k));
    const tail = nums.slice(nums.length - k);
    const head = nums.slice(0, nums.length - k);
    nums.splice(0, nums.length, ...tail, ...head);
 };

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    { nums: [1,2,3,4,5,6,7], k: 3, result: [5,6,7,1,2,3,4] },
    { nums: [-1,-100,3,99], k: 2, result: [3,99,-1,-100] },
];

describe.each(testcases)(`nums: $nums, k: $k`, ({ nums, k, result }) => {
    test(`returns`, () => {
        rotate(nums, k);
        expect(nums).toEqual(result);
    });
});
