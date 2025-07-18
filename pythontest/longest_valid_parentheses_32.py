# https://leetcode.cn/problems/longest-valid-parentheses/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length
