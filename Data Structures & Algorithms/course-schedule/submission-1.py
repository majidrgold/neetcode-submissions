class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # dfs
        # pre_map = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     pre_map[crs].append(pre)
        
        # visiting = set()

        # def dfs(crs):
        #     if crs in visiting:
        #         return False
        #     if pre_map[crs] == []:
        #         return True
            
        #     visiting.add(crs)
        #     for pre in pre_map[crs]:
        #         if not dfs(pre):
        #             return False
        #     visiting.remove(crs)
        #     pre_map[crs] = []
        #     return True
        
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        
        # return True
        # t: O(V+E), s: O(V+E)
        # -- BFS - Topological Sort (Kahn's Algorithm)
        pre_map = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            indegree[crs] += 1
            pre_map[pre].append(crs)

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for next_crs in pre_map[node]:
                indegree[next_crs] -= 1
                if indegree[next_crs] == 0:
                    q.append(next_crs)

        return finish == numCourses

        