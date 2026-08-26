# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # # 1. DFS by Me
        # count = 0
        # def dfs(node, max_val):
        #     nonlocal count
        #     if not node:
        #         return None
        #     if node.val >= max_val:
        #         count += 1
        #         max_val = node.val
        #     dfs(node.left, max_val)
        #     dfs(node.right, max_val)
            
        # dfs(root, -1e6)
        # return count
        # t: O(n), s: O(n)
        #
        # ---
        #
        # # 1.1 DFS by Neetcode
        # def dfs(node, max_val):
        #     if not node:
        #         return 0
            
        #     res = 1 if node.val >= max_val else 0
        #     max_val = max(max_val, node.val)
        #     res += dfs(node.left, max_val)
        #     res += dfs(node.right, max_val)

        #     return res 
        
        # return dfs(root, root.val)  
        # ---
        # ---
        # ---
        # 2. BFS      
        from collections import deque

        if not root:
            return 0

        q = deque()
        q.append((root, float('-inf')))
        res = 0
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                res += 1
                max_val = node.val
            if node.left:
                q.append((node.left, max_val))
            if node.right:
                q.append((node.right, max_val))
        
        return res

            

        