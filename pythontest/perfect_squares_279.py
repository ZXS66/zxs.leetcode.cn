# https://leetcode.cn/problems/perfect-squares/description/?envType=study-plan-v2&envId=top-100-liked


from math import isqrt
from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        # dp = [float('inf')] * (n + 1)
        # 1 <= n <= 10^4
        dp = [10001] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, isqrt(i) + 1):
                square = j * j
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]
