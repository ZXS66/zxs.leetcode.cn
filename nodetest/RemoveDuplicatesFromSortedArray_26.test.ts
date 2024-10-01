/** 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。 */
function removeDuplicates(nums: number[]): number {
    let i = 0;
    for (let j = 1; j < nums.length; j++) {
        if (nums[i] !== nums[j]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
};

// unit test
import { describe, expect, test } from '@jest/globals';
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
