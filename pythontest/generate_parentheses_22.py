# https://leetcode.cn/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(s, left, right):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack("", 0, 0)
        return res
