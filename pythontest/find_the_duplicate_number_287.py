# https://leetcode.cn/problems/find-the-duplicate-number/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Find the entrance to the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
