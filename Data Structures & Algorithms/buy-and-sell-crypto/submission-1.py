class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Brute Force
        n = len(prices)
        profit = 0
        profits = []
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = max(cur, prices[j] - prices[i])
            profits.append(cur)
        return max(profits)


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
        