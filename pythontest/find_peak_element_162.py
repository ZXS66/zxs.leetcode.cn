# https://leetcode.cn/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150

# 1. 你可以假设 nums[-1] = nums[n] = -∞ 。
# 2. 必须实现时间复杂度为 O(log n) 的算法来解决此问题
# 3. 返回 任何一个峰值 所在位置即可

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                # 右侧有可能是峰值，继续向右搜索
                left = mid
            else:
                # 左侧有可能是峰值，继续向左搜索
                right = mid
        
        return -1