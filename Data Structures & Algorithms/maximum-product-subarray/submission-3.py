class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # 1.Brute Force
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res, cur)
        #     for j in range(i + 1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res, cur)
        # return res
        # ---
        # 2. Sliding Window

        # 3. Kadane's Style
        res = nums[0]
        cur_min, cur_max = 1, 1
        for num in nums:
            tmp = cur_max * num
            cur_max = max(num * cur_max, num, num * cur_min)
            cur_min = min(tmp, num, num * cur_min)
            res = max(res, cur_max)

        return res





            