class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # 1. set 
        # return len(set(nums)) != len(nums)
        # # s: O(n), t: O(n)
        # 2. sort
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
        # s: O(1) t: O(nlogn)
        # # 3. Hash Map
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        # # # S: O(n), t: O(n)
        