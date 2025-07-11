# https://leetcode.cn/problems/sort-colors/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index, two_index = 0, len(nums) - 1
        i = 0
        while i <= two_index:
            if nums[i] == 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two_index] = nums[two_index], nums[i]
                two_index -= 1
            else:
                i += 1
