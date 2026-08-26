class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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

        # 4. Optimal
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

