# https://leetcode.cn/problems/longest-harmonious-subsequence/?envType=daily-question&envId=2025-06-30

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        keys = list(cnt.keys())
        if len(keys) == 1:
            return 0
        keys.sort()
        res = 0
        for i in range(1, len(keys)):
            if (keys[i] - keys[i - 1]) == 1:
                res = max(res, cnt[keys[i]] + cnt[keys[i - 1]])
        return res
