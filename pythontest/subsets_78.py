# https://leetcode.cn/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start: int, path: List[int]):
            res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
        