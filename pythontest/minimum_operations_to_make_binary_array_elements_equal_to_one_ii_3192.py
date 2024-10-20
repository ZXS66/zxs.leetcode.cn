# https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        prevVal = nums[0]
        operations = 1 if prevVal == 0 else 0
        for val in nums:
            if val == prevVal:
                continue
            prevVal = val
            operations += 1

        return operations
