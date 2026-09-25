class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]

sol = Solution()
print(sol.findMin(nums = [3,4,5,6,1,2]))
print(sol.findMin(nums = [4,5,0,1,2,3]))
print(sol.findMin(nums = [4,5,6,7]))

# edge cases
print(sol.findMin(nums = [1]))
print(sol.findMin(nums = [1,1,1,1,1]))



