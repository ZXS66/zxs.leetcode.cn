import { describe, expect, test } from '@jest/globals';
import removeDuplicates from './RemoveDuplicatesFromSortedArrayII_80';

const testcases = [
    { nums: [1, 1, 1, 2, 2, 3], k: 5 },
    { nums: [0, 0, 1, 1, 1, 1, 2, 3, 3], k: 7 },
    { nums: [1, 1, 1], k: 2 },
];

describe.each(testcases)(`nums: $nums, k: $k`, ({ nums, k }) => {
    test(`returns`, () => {
        expect(removeDuplicates(nums)).toBe(k);
    });
});
