# https://leetcode.cn/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        preMax, maxRes = nums[0], nums[0]
        preMin, minRes = nums[0], nums[0]
        sum = nums[0]
        for i in range(1, n):
            preMax = max(preMax + nums[i], nums[i])
            maxRes = max(maxRes, preMax)
            preMin = min(preMin + nums[i], nums[i])
            minRes = min(minRes, preMin)
            sum += nums[i]
        if maxRes < 0:
            return maxRes
        else:
            return max(maxRes, sum - minRes)
