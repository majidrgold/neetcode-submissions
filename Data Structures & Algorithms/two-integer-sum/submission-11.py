class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two path
        # complement = dict()
        # for i, num in enumerate(nums):
        #     complement[target - num] = i
        # for i, num in enumerate(nums):
        #     if num in complement:
        #         j = complement[num]
        #         if i != j:
        #             return [i, j]
        # O(n) O(n)

        seen = dict()
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i] 
            seen[num] = i
        
        return None