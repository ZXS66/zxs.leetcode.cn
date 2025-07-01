# https://leetcode.cn/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-06-28

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        res = []
        for n in nums:
            if len(res) < k:
                res.append(n)
            else:
                minValue = min(res)
                if minValue < n:
                    res.remove(minValue)
                    res.append(n)
        return res
