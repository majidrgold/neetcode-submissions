class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # 1.  DFS - sink-the-island
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # rows, cols = len(grid), len(grid[0])
        # count = 0
        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
        #         return
        #     grid[r][c] = "0"
        #     for dr, dn in directions:
        #         dfs(r + dr, c + dn)

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             count += 1

        # return count
        # # T: O(m∗n), M: O(m∗n)
        # ---
        # # 2. BFS
        dirrections = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            from collections import deque
            grid[r][c] = "0"
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirrections:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0": 
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands
        # # T: O(m∗n), M: O(m∗n)
        # ---
        # ---
        # 3. Disjoint Set Union
        





        