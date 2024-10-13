# https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/

from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # 暴力解决方案（嵌套for循环）不可行，因输入参数数值范围更大，会超时

        # 参考链接：https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/solutions/2928182/you-zhi-shu-dui-de-zong-shu-ii-by-leetco-obro/

        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        max1 = max(counter1)
        ans = 0
        for j, cnt2 in counter2.items():
            for i in range(j * k, max1 + 1, j * k):
                if i in counter1:
                    ans += counter1[i] * cnt2
        return ans
