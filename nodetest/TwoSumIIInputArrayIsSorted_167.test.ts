// https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

function twoSum(numbers: number[], target: number): number[] {
    let left = 0;
    let right = numbers.length - 1;
    while (left < right) {
        const sum = numbers[left] + numbers[right];
        if (sum === target) {
            return [left + 1, right + 1];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return [];
};


// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    { numbers: [2, 7, 11, 15], target: 9, result: [1, 2] },
    { numbers: [2, 3, 4], target: 6, result: [1, 3] },
    { numbers: [-1, 0], target: -1, result: [1, 2] },
];

describe.each(testcases)(`numbers: $numbers, target: $target`, ({ numbers, target, result }) => {
    test(`returns ${result}`, () => {
        const whatyougot = twoSum(numbers, target);
        expect(whatyougot).toEqual(result);
    });
});
