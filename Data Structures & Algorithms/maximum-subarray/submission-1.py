class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_sum = nums[0]

        subarray_sum = 0
        for num in nums:
            if subarray_sum < 0:
                subarray_sum = 0
            subarray_sum += num
            max_sum = max(subarray_sum, max_sum)
        
        return max_sum
