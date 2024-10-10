// https://leetcode.cn/problems/find-the-number-of-good-pairs-i/description/

function numberOfPairs(nums1: number[], nums2: number[], k: number): number {
    const n = nums1.length;
    const m = nums2.length;
    let ans = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (nums1[i] % (nums2[j] * k) === 0) {
                // 如果 nums1[i] 可以被 nums2[j] * k 整除，则称数对 (i, j) 为 优质数对
                ans++;
            }
        }
    }

    return ans;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums1: [1, 3, 4], nums2: [1, 3, 4], k: 1, result: 5 },
    { nums1: [1, 2, 4, 12], nums2: [2, 4], k: 3, result: 2 },
];

describe.each(testcases)(`nums1: $nums1, nums2:$nums2, k:$k`, ({ nums1, nums2, k, result }) => {
    test(`returns ${result}`, () => {
        expect(numberOfPairs(nums1, nums2, k)).toBe(result);
    });
});