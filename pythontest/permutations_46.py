# https://leetcode.cn/problems/permutations/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()
        backtrack([])
        return res