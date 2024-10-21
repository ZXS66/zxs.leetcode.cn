# https://leetcode.cn/problems/smallest-range-ii/description/

# Reference: https://leetcode.cn/problems/smallest-range-i/description/

from itertools import pairwise
from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        min_val, max_val = min(nums), max(nums)
        if max_val - min_val <= k:
            # 场景一：最大值和最小值相差小于等于k，则更改（同时+k或者-k均可）后的最小值保持不变
            return max_val - min_val
        
        # k < max_val - min_val < 3k
        ans = max_val - min_val # 最差结果，同场景一
        # 尝试查找小于这种结果的变动
        nums.sort()
        for a,b in pairwise(nums):
            max_temp = max(a+k, max_val-k)
            min_temp = min(min_val+k, b-k)
            ans = min(ans, max_temp - min_temp)
        
        return ans
