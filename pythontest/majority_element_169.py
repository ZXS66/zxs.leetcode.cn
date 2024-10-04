# https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
        return -1
        

