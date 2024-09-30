import { describe, expect, test } from '@jest/globals';
import { removeDuplicates } from './RemoveDuplicatesFromSortedArray_26';

const testcases = [
    {
        nums: [1, 1, 2],
        k: 2
    },
    {
        nums: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        k: 5
    }
];

describe.each(testcases)(`nums: $nums, k: $k`, ({ nums, k }) => {
    test(`returns ${k}`, () => {
        expect(removeDuplicates(nums)).toBe(k);
    });
});
