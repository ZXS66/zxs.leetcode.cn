// https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

function maxArea(height: number[]): number {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;
    while (left < right) {
        const area = Math.min(height[left], height[right]) * (right - left);
        maxArea = Math.max(maxArea, area);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxArea;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { height: [1, 8, 6, 2, 5, 4, 8, 3, 7], result: 49 },
    { height: [1, 1], result: 1 },
    { height: [4, 3, 2, 1, 4], result: 16 },
];

describe.each(testcases)(`height: $height`, ({ height, result }) => {
    test(`returns ${result}`, () => {
        expect(maxArea(height)).toBe(result);
    });
});
