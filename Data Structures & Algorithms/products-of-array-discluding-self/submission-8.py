class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. 
        # n = len(nums)
        # prefix, suffix = [1] * n, [1] * n
        # res = []
        # cur = 1
        # for i in range(n):
        #     prefix[i] = cur
        #     cur *= nums[i]
        # cur = 1
        # for j in range(n - 1, -1 , -1):
        #     suffix[j] = cur
        #     cur *= nums[j]

        # for i in range(n):
        #     res.append(prefix[i] * suffix[i])
        
        # return res
        # t: O(n), s: O(n)
        # 2. Optimised
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        
        return res

