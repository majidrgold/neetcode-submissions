class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = dict()
        for i, num in enumerate(nums):
            complement[target - num] = i
        for i, num in enumerate(nums):
            if num in complement:
                j = complement[num]
                if i != j:
                    return [i, j]
        