class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution would be O(n2) to search all pairs in nums
        # We can use hash map for this problem
        # in can be done in two path, one path we can go through it
        # and get index of each value 
        # second path we get position,
        # we can also do it in one path
        
        # counts = {}

        # for i, num in enumerate(nums):
        #     complement = target - num
        #     counts[complement] = i
        
        # for i, num in enumerate(nums):
        #     if num in counts and counts[num] != i:
        #         return [i, counts[num]]

        # return -1

        # # one path
        counts = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in counts:
                return [counts[num], i]
            
            counts[complement] = i

        return -1
            

        