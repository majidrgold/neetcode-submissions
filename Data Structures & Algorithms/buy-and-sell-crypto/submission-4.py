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
        # t: O(n^2), s: O(1)
        # 2. Two pointer
        n = len(prices)
        l, r = 0, 1
        maxP = 0
        while r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                r += 1
            else: 
                l = r
                r += 1
        return maxP


        # # 3. Danamic Prgraming
        # n = len(prices)
        # profit = 0
        # buy = prices[0]
        # for sell in prices:
        #     profit = max(profit, sell - buy)
        #     buy = min(buy, sell)
        # return profit
        # t: O(n), s: O(1)
        