class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Brute Force
        n = len(nums)
        sums = []
        for i in range(n):
            moving_sum, max_sumi = nums[i], nums[i]
            for j in range(i + 1, n):
                moving_sum += nums[j]
                if moving_sum > max_sumi:
                    max_sumi = moving_sum
            sums.append(max_sumi)
        return max(sums)

