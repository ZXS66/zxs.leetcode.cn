import { describe, expect, test } from '@jest/globals';
import { removeElement } from "./RemoveElement_27";


// test cases
const testcases = [
    { nums: [3, 2, 2, 3], val: 3, result: 2 },
    { nums: [0, 1, 2, 2, 3, 0, 4, 2], val: 2, result: 5 },
];

describe.each(testcases)(`nums: $nums, val: $val`, ({ nums, val, result }) => {
    test(`returns ${result}`, () => {
        const k = removeElement(nums, val);
        expect(k).toBe(result);
    });
});
