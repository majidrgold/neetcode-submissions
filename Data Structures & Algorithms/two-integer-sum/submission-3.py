class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1. brute force o(n2)
        # 2. two pass hash map O(n) s: n
        # 1. one pass hash map O(n) s: n
        indices = {}
        for i, num in enumerate(nums):
            if num in indices:
                return [indices[num], i]
            indices[target - num] = i
        