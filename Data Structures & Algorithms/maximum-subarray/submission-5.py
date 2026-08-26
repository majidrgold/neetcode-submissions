class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # 1. Brute Force
        # n, res = len(nums), nums[0]
        # for i in range(n):
        #     curr = 0
        #     for j in range(i, n):
        #         curr += nums[j]
        #         res = max(curr, res)
        # return res
        # # t: O(n^2), s.res: O(1), s.ext = O(1)
        # # 2. Recursion
        # def dfs(i, flag):
        #     if i == len(nums):
        #         return 0 if flag else -1e6
        #     if flag:
        #         return max(0, nums[i] + dfs(i + 1, True))
        #     return max(dfs(i + 1, False), nums[i] + dfs(i+1, True))
        # return dfs(0, False)
        # # t: O(2^n) s: O(n)
        # 3. Dynamic Programming - Top-down
        memo = [[None] * 2 for _ in range(len(nums) + 1)]

        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1e6
            if memo[i][flag] is not None:
                return memo[i][flag]
            if flag:
                memo[i][flag] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[i][flag] = max(dfs(i + 1, False), 
                                    nums[i] + dfs(i + 1, True))
            return memo[i][flag]

        return dfs(0, False) 
        # t: O(n), s: O(n)


        
        




