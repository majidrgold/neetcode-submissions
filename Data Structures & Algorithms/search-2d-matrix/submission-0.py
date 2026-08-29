class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # 1. Brute Force
        # m, n = len(matrix), len(matrix[0])
        
        # for r in range(m - 1):
        #     for c in range(n - 1):
        #         if matrix[r][c] == target:
        #             return True
        
        # return False
        # -- t: O(m *n), s: O(1)
        # 2. search row and col seaprately
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False


        