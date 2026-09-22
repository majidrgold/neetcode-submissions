class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            
            mid = (left + right) // 2
            r, c = mid // cols, mid % cols 
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False