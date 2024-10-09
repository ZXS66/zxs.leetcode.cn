// https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/description/

function minimumDifference(nums: number[], k: number): number {
    const n = nums.length;
    if (n === 1) {
        return Math.abs(k - nums[0]);
    }
    const bitsMaxPos = new Array(31).fill(-1);
    let res = Number.MAX_SAFE_INTEGER;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= 30; j++) {
            if (nums[i] >> j & 1) {
                bitsMaxPos[j] = i;
            }
        }
        const posToBit: [number, number][] = [];
        for (let j = 0; j <= 30; j++) {
            if (bitsMaxPos[j] !== -1) {
                posToBit.push([bitsMaxPos[j], j]);
            }
        }
        posToBit.sort((a, b) => b[0] - a[0]);
        let val = 0;
        for (let j = 0, p = 0; j < posToBit.length; p = j) {
            while (j < posToBit.length && posToBit[j][0] === posToBit[p][0]) {
                val |= 1 << posToBit[j][1];
                j++;
            }
            res = Math.min(res, Math.abs(val - k));
        }
    }
    return res;
    // 作者：力扣官方题解
    // 链接：https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/solutions/2942313/zhao-dao-an-wei-huo-zui-jie-jin-k-de-zi-gianx/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { nums: [1, 2, 4, 5], k: 3, result: 0 },
    { nums: [1, 3, 1, 3], k: 2, result: 1 },
    { nums: [1], k: 10, result: 9 },
];

describe.each(testcases)(`nums: $nums, k:$k`, ({ nums, k, result }) => {
    test(`returns ${result}`, () => {
        expect(minimumDifference(nums, k)).toBe(result);
    });
});