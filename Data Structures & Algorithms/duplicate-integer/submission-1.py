class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # method 1: Hashset
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # method 2: Hash set Length
        return len(set(nums)) < len(nums)

        

        