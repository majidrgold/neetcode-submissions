class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        # 1. sort --> t: nlogn, s:n (depend on sort method)
        # 2. len(list and lenset) --> t:n, s:n
        # 3. counter if exist then return o:n, s:n
        counter = {}
        for num in nums:
            if num in counter:
                return True
            counter[num] = 1
        return False