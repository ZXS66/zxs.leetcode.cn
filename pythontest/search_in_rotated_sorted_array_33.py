# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1
        if nums[0] == target:
            return 0
        n = len(nums)
        # 1. 确定旋转点
        rotate_idx = 0
        left, right = 0, n - 1
        while left<=right:
            mid = (left + right) // 2
            if nums[0]<=nums[mid]:
                # 旋转点在mid的右侧
                left = mid + 1
            else:
                # 旋转点在mid的左侧
                right = mid - 1
            rotate_idx = left
        
        # 2. 二分查找（此时，数组 nums[rotate_idx:] + nums[0:rotate_idx] 是升序的）
        left, right = rotate_idx, rotate_idx + n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid%n] == target:
                return mid%n
            elif nums[mid%n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
