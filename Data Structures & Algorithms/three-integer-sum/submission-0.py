class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sums = []
        for i in range(n):
            # Skip duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    sums.append([nums[i], nums[l], nums[r]])


                    # Skip duplicates for left pointer
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Skip duplicates for right pointer
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    # Move both pointers
                    l += 1
                    r -= 1
        return sums



        
        