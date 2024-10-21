# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        n = len(nums)
        min_val = nums[0]
        if n == 1:
            return nums[0]
        elif nums[-1]>nums[0]:
            # 没有旋转(0次旋转)
            return nums[0]
        left, right = 0, n - 1
        # 1. 确定旋转点
        while left<=right:
            mid = (left + right) // 2
            if nums[0]<=nums[mid]:
                # 旋转点在mid的右侧
                left = mid + 1
            else:
                # 旋转点在mid的左侧
                right = mid - 1
            min_val = nums[left]
        return min_val