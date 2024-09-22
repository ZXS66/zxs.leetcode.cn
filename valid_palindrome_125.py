# https://leetcode.cn/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]
