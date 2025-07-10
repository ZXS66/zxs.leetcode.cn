# https://leetcode.cn/problems/maximum-product-subarray/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_product = float('-inf')
        # current_product = 1
        # for num in nums:
        #     current_product *= num
        #     max_product = max(max_product, current_product, num)
        #     if current_product == 0:
        #         current_product = 1
        # return max_product

        maxF, minF, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mn = maxF, minF
            maxF = max(mx * nums[i], nums[i], mn * nums[i])
            minF = min(mn * nums[i], nums[i], mx * nums[i])
            if minF < (-1 << 31):
                minF = nums[i]
            ans = max(maxF, ans)
        return ans
