class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Brute Force
        n = len(prices)
        res = 0
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                res = max(res, sell - buy)
        return res


        # # 2. 
        # n = len(prices)
        # profit = 0
        # buy_p = prices[0]
        # for i in range(1, n):
        #     profit = max(profit, prices[i] - buy_p)
        #     if prices[i] < buy_p:
        #         buy_p = prices[i]
        # return profit
        # t: O(n), s: O(1)
        