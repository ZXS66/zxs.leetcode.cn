// https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
function threeSum(nums: number[]): number[][] {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const res: number[][] = [];
    for (let i = 0; i < n; i++) {
        // 剪枝
        if (nums[i] > 0) break;
        // 去重
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        let left = i + 1;
        let right = n - 1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum > 0) {
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                res.push([nums[i], nums[left], nums[right]]);
                // 去重
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;
                left++;
                right--;
            }
        }
    }
    return res;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [-1, 0, 1, 2, -1, -4], result: [[-1, -1, 2], [-1, 0, 1]] },
    { nums: [0, 1, 1], result: [] },
    { nums: [0, 0, 0], result: [[0, 0, 0]] },
];

describe.each(testcases)(`nums:$nums`, ({ nums, result }) => {
    test(`returns ${result}`, () => {
        const output = threeSum(nums);
        expect(output.length).toBe(result.length);
        if (output.length) {
            output.forEach((item) => {
                expect(item.length).toBe(3);
                expect(item.reduce((a, b) => a + b)).toBe(0);
            });
        }
    });
});
