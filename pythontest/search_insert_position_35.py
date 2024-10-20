# https://leetcode.cn/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150

# 必须使用时间复杂度为 O(log n) 的算法。

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left