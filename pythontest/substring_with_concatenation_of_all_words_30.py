# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150

from functools import cache
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n = len(s)
        m = len(words)
        k = len(words[0])
        if n < m * k:
            return []

        @cache
        def isValidSubString(subStr: str) -> bool:
            if len(subStr) != m * k:
                return False
            occurs = Counter(words)
            for i in range(0, m * k, k):
                word = subStr[i : i + k]
                if word in words:
                    occurs[word] -= 1
                    if occurs[word] < 0:
                        return False
                else:
                    return False
            return True

        res = []
        for i in range(0, n - m * k + 1):
            if isValidSubString(s[i : i + m * k]):
                res.append(i)

        return res
