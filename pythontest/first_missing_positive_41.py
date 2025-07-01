# https://leetcode.cn/problems/first-missing-positive/description/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1]) # -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
