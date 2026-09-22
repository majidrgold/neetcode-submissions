class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # solution 1
        # if not nums:
        #     return False
        # return len(set(nums)) != len(nums)
        # # O(n)O(1)
        # solution 2:
        if not nums:
            return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

        