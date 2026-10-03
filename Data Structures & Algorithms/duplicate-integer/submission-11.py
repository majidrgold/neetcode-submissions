class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) > len(set(nums))
        # # O(n), O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        