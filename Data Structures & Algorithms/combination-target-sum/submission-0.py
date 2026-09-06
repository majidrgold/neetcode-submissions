class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start_index, current_sum, curr):
            if current_sum == target:
                res.append(curr.copy())
                return
            if current_sum > target:
                return
            
            for i in range(start_index, len(nums)):
                curr.append(nums[i])
                backtrack(i, current_sum + nums[i], curr)
                curr.pop()
        
        backtrack(0, 0, [])
    
        return res
            

        