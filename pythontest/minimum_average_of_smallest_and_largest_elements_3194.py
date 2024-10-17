# https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/description/

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        n = len(nums)
        nums.sort()
        ans = nums[-1]
        # n 为偶数，需要重复 n / 2 次
        for i in range(int(n/2)):
            tmp = (nums[i] + nums[n-i-1]) / 2
            if tmp < ans: ans = tmp
        return ans
