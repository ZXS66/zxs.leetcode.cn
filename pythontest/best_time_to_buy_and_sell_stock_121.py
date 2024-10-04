# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # n = len(prices)
        # max = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if prices[j] > prices[i] and prices[j] - prices[i] > max:
        #             max = prices[j] - prices[i]
        # return max

        cost = 65536  # 0 <= prices[i] <= 10^4
        profit = 0  # max profit
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
