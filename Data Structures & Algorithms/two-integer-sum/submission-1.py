class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in count:
                return [count[comp], i]
            count[num] = i

        return None
        