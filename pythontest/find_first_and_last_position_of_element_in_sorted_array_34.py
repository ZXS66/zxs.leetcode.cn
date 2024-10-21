# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        elif n == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = right = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < n - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
        
        return [-1, -1]