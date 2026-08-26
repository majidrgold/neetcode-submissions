class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # 1. Brute Force
        # n = len(nums)
        # res = [0] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(0, n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
            
        #     res[i] = prod
        # return res
        # # t: O(n^2), s.ext: O(1), s.res: O(n)

        # 2. Devision 
        n = len(nums)
        res = [0] * n

        prod = 1
        zero_cnt = 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1: return [0] * n

        for i, c in enumerate(nums):
            if zero_cnt: 
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
            
        return res
        
        # # 3. prefix and Suffix
        # n = len(nums)
        # pref = [0] * n
        # suff = [0] * n
        # res = [0] * n

        # pref[0] = suff[n - 1] = 1
        # for i in range(1, n):
        #     pref[i] = pref[i - 1] * nums[i - 1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = suff[i + 1] * nums [i + 1]
        # for i in range(n):
        #     res[i] = suff[i] * pref[i]
        # t: O(n), s.ext: O(n), s.res: O(n)

        # # 4. Optimal
        # n = len(nums)
        # res = [1] * n

        # prefix = 1
        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(n - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # t: O(n), s.ext: O(1), s.res: O(n)

        return res

