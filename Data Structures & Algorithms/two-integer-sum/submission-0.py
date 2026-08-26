class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in prevMap:
                return [prevMap[complement], i]
            prevMap[num] = i 