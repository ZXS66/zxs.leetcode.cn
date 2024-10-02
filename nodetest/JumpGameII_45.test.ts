// https://leetcode.cn/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

function jump(nums: number[]): number {
    const n = nums.length;
    if (n === 1) {
        return 0;
    }
    if (n === 2 && nums[0] >= 1) {
        return 1;
    }
    // 贪心算法
    let cur = 0;
    let end = 0;
    let move = 0;
    for (let i = 0; i < n - 1; i++) {
        // 下一步，挪到可以下下步能挪到的最远的地方
        cur = Math.max(cur, i + nums[i]);
        if (i === end) {
            end = cur;
            move++;
        }
    }
    return move;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [2, 3, 1, 1, 4], result: 2 },
    { nums: [2, 3, 0, 1, 4], result: 2 },
];

describe.each(testcases)(`nums: $nums`, ({ nums, result }) => {
    test(`returns ${result}`, () => {
        expect(jump(nums)).toBe(result);
    });
});

