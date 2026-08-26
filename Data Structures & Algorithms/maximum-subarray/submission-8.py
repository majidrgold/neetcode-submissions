class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ---
        # # 1. Brute Force
        # n, res = len(nums), nums[0]
        # for i in range(n):
        #     curr = 0
        #     for j in range(i, n):
        #         curr += nums[j]
        #         res = max(curr, res)
        # return res
        # # t: O(n^2), s.res: O(1), s.ext = O(1)
        # ---
        # # 2. Recursion
        # def dfs(i, flag):
        #     if i == len(nums):
        #         return 0 if flag else -1e6
        #     if flag:
        #         return max(0, nums[i] + dfs(i + 1, True))
        #     return max(dfs(i + 1, False), nums[i] + dfs(i+1, True))
        # return dfs(0, False)
        # # t: O(2^n) s: O(n)
        # ---
        # # 3. Dynamic Programming - Top-down
        # memo = [[None] * 2 for _ in range(len(nums) + 1)]

        # def dfs(i, flag):
        #     if i == len(nums):
        #         return 0 if flag else -1e6
        #     if memo[i][flag] is not None:
        #         return memo[i][flag]
        #     if flag:
        #         memo[i][flag] = max(0, nums[i] + dfs(i + 1, True))
        #     else:
        #         memo[i][flag] = max(dfs(i + 1, False), 
        #                             nums[i] + dfs(i + 1, True))
        #     return memo[i][flag]

        # return dfs(0, False) 
        # # t: O(n), s: O(n)
        # ---
        # # 4. Dynamic Programming : Bottom-Up
        # n = len(nums)
        # dp = [[None] * 2 for _ in range(n)]
        # dp[n - 1][0] = dp[n - 1][1] = nums[n - 1]

        # for i in range(n - 2, -1, -1):
        #     dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1])
        #     dp[i][0] = max(dp[i + 1][0], dp[i][1])

        # return dp[0][0]
        # # t: O(n) s: O(n)
        # ---
        # # 5. Dynamic Programming (Space Optimized)
        # dp = [*nums]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # return max(dp)
        # # t: O(n), s:O(n)
        # ---
        # 6. Kadane's Algo
        n = len(nums)
        curr = nums[0]
        mx = nums[0]

        for i in range(1, n):
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]
            mx = max(curr, mx)

        return mx




            






        
        




