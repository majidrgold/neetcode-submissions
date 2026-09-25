class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        lo, hi = 0,  rows * cols - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
    
sol = Solution()
print(sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))
print(sol.searchMatrix([], target = 10))
print(sol.searchMatrix([[1]], target = 10))

        