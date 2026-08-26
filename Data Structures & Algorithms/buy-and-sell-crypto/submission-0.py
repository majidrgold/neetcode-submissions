class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        buy_p = prices[0]
        for i in range(1, n):
            profit = max(profit, prices[i] - buy_p)
            if prices[i] < buy_p:
                buy_p = prices[i]
        return profit
        