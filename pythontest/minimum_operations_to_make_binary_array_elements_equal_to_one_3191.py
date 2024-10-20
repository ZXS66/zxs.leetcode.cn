# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        for i in range(len(nums) - 2):
            if nums[i] == 1:
                continue
            nums[i] = 1
            nums[i + 1] = 1 if nums[i + 1] == 0 else 0
            nums[i + 2] = 1 if nums[i + 2] == 0 else 0
            operations += 1
        return operations if nums[-2] == 1 and nums[-1] == 1 else -1
