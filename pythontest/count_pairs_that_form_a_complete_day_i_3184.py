# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-i/description/
# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/description/

from typing import List
from math import factorial

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hour_count = [0]*24
        for h in hours:
            hour_count[h%24]+=1
        ans = 0
        for i in range(13):
            count = hour_count[i]
            if i == 0:
                # 组合公式，阶乘法
                if count>=2:
                    ans+=factorial(count) // (factorial(2) * factorial(count - 2))
            elif i == 12:
                if count>=2:
                    ans += factorial(count) // (factorial(2) * factorial(count-2))
            else:
                ans+= count * hour_count[24-i]
        return ans
