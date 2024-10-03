// https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150


function productExceptSelf(nums: number[]): number[] {
    // const resultLeft = new Array();
    // let base = 1;
    // for (let i = 0; i < nums.length; i++) {
    //     resultLeft[i] = base;
    //     base *= nums[i];
    // }
    // base = 1;
    // let resultRight = new Array();
    // for (let i = nums.length - 1; i >= 0; i--) {
    //     resultRight[i] = base;
    //     base *= nums[i];
    // }
    // const result = new Array();
    // for (let i = 0; i < nums.length; i++) {
    //     result[i] = resultLeft[i] * resultRight[i];
    // }
    // return result;
    const result = new Array();
    let base = 1;
    for (let i = 0; i < nums.length; i++) {
        result[i] = base;
        base *= nums[i];
    }
    base = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        result[i] *= base;
        base *= nums[i];
    }
    return result;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [1, 2, 3, 4], result: [24, 12, 8, 6] },
    { nums: [-1, 1, 0, -3, 3], result: [0, 0, 9, 0, 0] },
];

describe.each(testcases)(`nums: $nums, result: $result`, ({ nums, result }) => {
    test(`returns ${result}`, () => {
        // expect(productExceptSelf(nums)).toEqual(result);
        // expect(-0).toBe(0);  // failed!!!
        const output = productExceptSelf(nums);
        expect(JSON.stringify(output)).toBe(JSON.stringify(result));
    });
});
