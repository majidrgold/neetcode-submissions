class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def backtrack(start_index, current_sum, cur):
            if current_sum == target:
                res.append(cur.copy())
                return
            if current_sum > target:
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], cur)
                cur.pop()
        
        backtrack(0, 0, [])
    
        return res


        