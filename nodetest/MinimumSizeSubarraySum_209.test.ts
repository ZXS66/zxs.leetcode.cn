// https://leetcode.cn/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

function minSubArrayLen(target: number, nums: number[]): number {
    // const n = nums.length;
    // nums.sort((a, b) => b - a);
    // let sum = 0;
    // for (let i = 0; i < n; i++) {
    //     sum += nums[i];
    //     if (sum >= target) {
    //         return i + 1;
    //     }
    // }
    // return 0;
    // 子数组 是数组中 连续的 非空 元素序列！！！
    let left = 0;
    let right = 0;
    let sum = 0;
    let minLength = Infinity;
    while (right < nums.length) {
        sum += nums[right];
        while (sum >= target) {
            minLength = Math.min(minLength, right - left + 1);
            sum -= nums[left];
            left++;
        }
        right++;
    }
    return minLength === Infinity ? 0 : minLength;
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { target: 7, nums: [2, 3, 1, 2, 4, 3], result: 2 },
    { target: 4, nums: [1, 4, 4], result: 1 },
    { target: 11, nums: [1, 1, 1, 1, 1, 1, 1, 1], result: 0 },
    { target: 15, nums: [1, 2, 3, 4, 5], result: 5 },
    { target: 213, nums: [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12], result: 8 }
];

describe.each(testcases)(`target: $target, nums: $nums`, ({ target, nums, result }) => {
    test(`returns ${result}`, () => {
        expect(minSubArrayLen(target, nums)).toBe(result);
    });
});
