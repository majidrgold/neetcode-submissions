class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # 1. Tow Pointer
        # nums.sort()
        # n = len(nums)
        # sums = []
        # for i in range(n):
        #     # Skip duplicate starting values
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     target = - nums[i]
        #     l, r = i + 1, n - 1
        #     while l < r:
        #         if nums[l] + nums[r] > target:
        #             r -= 1
        #         elif nums[l] + nums[r] < target:
        #             l += 1
        #         else:
        #             sums.append([nums[i], nums[l], nums[r]])


        #             # Skip duplicates for left pointer
        #             while l < r and nums[l] == nums[l+1]:
        #                 l += 1
        #             # Skip duplicates for right pointer
        #             while l < r and nums[r] == nums[r-1]:
        #                 r -= 1
                    
        #             # Move both pointers
        #             l += 1
        #             r -= 1
        # return sums
        # # t: O(n ^ 2), s: O(n) or O(1) depend on sorting algo, s_res: O(m)
        # ---
        # 2. Hash map
        nums.sort()
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        res = []

        for i in range(n):
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                
                target = - (nums[i] + nums[j])
                if target in count and count[target] > 0:
                    res.append([nums[i], nums[j], target])
                
            for j in range(i + 1, n):
                count[nums[j]] += 1

        return res




        
        