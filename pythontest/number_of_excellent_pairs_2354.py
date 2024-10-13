# https://leetcode.cn/problems/number-of-excellent-pairs/description/

from collections import Counter

class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        cnt = Counter(x.bit_count() for x in set(nums))
        ans = 0
        for ones1, nums1 in cnt.items():
            for ones2, nums2 in cnt.items():
                if ones1 + ones2 >= k:  
                    # num1 OR num2 和 num1 AND num2 的二进制表示中值为 1 的位数之和大于等于 k
                    # 等效于计算 num1 x和 num2 本身 bit 为 1 的位数和
                    ans += nums1 * nums2
        return ans
