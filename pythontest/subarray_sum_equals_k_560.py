# https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked

# 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # amount = 0
        # current_sum = 0
        # for left in range(0, len(nums)):
        #     current_sum += nums[left]
        #     if current_sum == k:
        #         amount += 1
        #     for right in range(left + 1, len(nums)):
        #         current_sum += nums[right]
        #         if current_sum == k:
        #             amount += 1
        #     current_sum = 0
        # return amount

        ans = s = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[s] += 1
            s += x
            ans += cnt[s - k]
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/subarray-sum-equals-k/solutions/2781031/qian-zhui-he-ha-xi-biao-cong-liang-ci-bi-4mwr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

