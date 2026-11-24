class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force
        # t: O(n^2), S: O(1)
        # Sort
        # t: O(nlogn) s: O(n)
        # # hash-set
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        # # O(n), O(n)
        set
        return len(set(nums)) < len(nums)
        O(n), O(n)