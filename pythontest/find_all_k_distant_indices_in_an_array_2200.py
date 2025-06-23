# https://leetcode.cn/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        indices = [i for i, num in enumerate(nums) if num == key]
        result = set()

        for index in indices:
            start = max(0, index - k)
            end = min(n - 1, index + k)
            for i in range(start, end + 1):
                result.add(i)

        return sorted(result)