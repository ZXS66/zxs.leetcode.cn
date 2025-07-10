# https://leetcode.cn/problems/find-lucky-integer-in-an-array/description/?envType=daily-question&envId=2025-07-05

from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # count = {}
        # for num in arr:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        
        # lucky_integer = -1
        # for num, freq in count.items():
        #     if num == freq:
        #         lucky_integer = max(lucky_integer, num)

        # return lucky_integer
        
        cnt = Counter(arr)
        lucky_integer = -1
        for num, freq in cnt.items():
            if num == freq:
                lucky_integer = max(lucky_integer, num)
        return lucky_integer