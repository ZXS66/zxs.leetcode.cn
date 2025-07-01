# https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solutions/310424/man-zu-tiao-jian-de-zi-xu-lie-shu-mu-by-leetcode-s/?envType=daily-question&envId=2025-06-29


# from bisect import bisect


import bisect

class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        n = len(nums)
        P = 10**9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if nums[i] * 2 > target:
                break
            maxValue = target - nums[i]
            pos = bisect.bisect_right(nums, maxValue) - 1
            contribute = f[pos - i] if pos >= i else 0
            ans += contribute

        return ans % P
