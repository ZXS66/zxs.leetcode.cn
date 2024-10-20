# https://leetcode.cn/problems/smallest-range-i/description/


from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        return max(0, max(nums) - min(nums) - 2 * k)
