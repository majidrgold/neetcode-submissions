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
        # m, n = len(matrix), len(matrix[0])
        # r, c = 0, n - 1
        # while r < m and c >= 0:
        #     if matrix[r][c] > target:
        #         c -= 1
        #     elif matrix[r][c] < target:
        #         r += 1
        #     else:
        #         return True
        # return False
        # 3. Binary search
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
    
        return False

        # t: O(logn + logn) --> O(log(m*n)), s: O(1)
        # 4. Binary Search (One Pass):
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = (l + r) // 2
            row = m // COLS
            col = m % COLS
            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
        return False






        