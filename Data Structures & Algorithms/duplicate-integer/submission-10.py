class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # solution 1
        # return len(set(nums)) != len(nums)
        # # O(n)O(n)
        # solution 2:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        # # O(n)O(n)


        