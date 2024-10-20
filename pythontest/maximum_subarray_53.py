# https://leetcode.cn/problems/maximum-subarray/solutions/228009/zui-da-zi-xu-he-by-leetcode-solution/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev, ans = 0, nums[0]
        for v in nums:
            prev = max(v, prev + v)
            ans = max(ans, prev)
        return ans
