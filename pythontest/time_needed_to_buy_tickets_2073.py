# https://leetcode.cn/problems/time-needed-to-buy-tickets/description/

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        n = len(tickets)
        ans = 0
        for i in range(n):
            if i <= k:
                ans += min(tickets[i], tickets[k])
            else:
                ans += min(tickets[i], tickets[k] - 1)
        return ans
