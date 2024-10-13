# https://leetcode.cn/problems/egg-drop-with-2-eggs-and-n-floors/description/


class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n < 2:
            return n
        for i in range(2, n):
            if i * (i + 1) / 2 >= n:
                return i
        return n