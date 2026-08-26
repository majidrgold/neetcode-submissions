class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # 1. Brute Force
        # n = len(prices)
        # res = 0
        # for i in range(n):
        #     buy = prices[i]
        #     for j in range(i + 1, n):
        #         sell = prices[j]
        #         res = max(res, sell - buy)
        # return res


        # # 2. Danamic Prgraming
        n = len(prices)
        profit = 0
        buy = prices[0]
        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit
        # t: O(n), s: O(1)
        