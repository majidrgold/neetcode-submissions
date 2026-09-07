class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = [False] * len(nums)

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])
                backtrack()
                cur.pop()
                used[i] = False
        
        backtrack()

        return res
        