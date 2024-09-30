import { describe, expect, test } from '@jest/globals';
import { merge } from './MergeSortedArray_88';

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