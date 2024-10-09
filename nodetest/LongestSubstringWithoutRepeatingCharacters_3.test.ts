// https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

function lengthOfLongestSubstring(s: string): number {
    let maxLength = 0;
    let left = 0;
    let right = 0;
    const charSet = new Set<string>();

    while (right < s.length) {
        const char = s[right];
        if (!charSet.has(char)) {
            charSet.add(char);
            maxLength = Math.max(maxLength, right - left + 1);  // 更新最大长度
            right++;
        } else {
            charSet.delete(s[left]);
            left++;
        }
    }
    return maxLength;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { s: "abcabcbb", result: 3 },
    { s: "bbbbb", result: 1 },
    { s: "pwwkew", result: 3 },
];

describe.each(testcases)(`s:$s`, ({ s, result }) => {
    test(`returns ${result}`, () => {
        expect(lengthOfLongestSubstring(s)).toBe(result);
    });
});

