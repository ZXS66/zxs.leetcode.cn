# https://leetcode.cn/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
