/** Do not return anything, modify nums1 in-place instead. */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    const swap: number[] = [];
    while (m > 0 || n > 0) {
        if (m > 0 && n > 0) {
            if (nums1[m - 1] > nums2[n - 1]) {
                swap.push(nums1[m - 1]);
                m--;
            } else {
                swap.push(nums2[n - 1]);
                n--;
            }
        } else if (m > 0) {
            swap.push(nums1[m - 1]);
            m--;
        } else {
            swap.push(nums2[n - 1]);
            n--;
        }
    }
    for (let i = 0; i < swap.length; i++) {
        nums1[i] = swap[swap.length - i - 1];
    }
};

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        nums1: [1, 2, 3, 0, 0, 0],
        m: 3,
        nums2: [2, 5, 6],
        n: 3
    },
    {
        nums1: [1],
        m: 1,
        nums2: [],
        n: 0
    },
    {
        nums1: [0],
        m: 0,
        nums2: [1],
        n: 1
    },
];


describe.each(testcases)(`nums1: $nums1, m: $m, nums2: $nums2, n:$n`, ({ nums1, m, nums2, n }) => {
    test(`returns`, () => {
        const lengthBeforeMerged = nums1.length;
        merge(nums1, m, nums2, n);
        expect(nums1.length).toBeGreaterThanOrEqual(lengthBeforeMerged);
    });
});