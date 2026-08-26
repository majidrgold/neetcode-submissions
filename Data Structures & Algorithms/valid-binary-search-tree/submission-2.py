# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # 1. DFS
        # def dfs(node, min_val, max_val):
        #     if not node:
        #         return True
        #     left, right = node.left, node.right
        #     if not min_val < node.val < max_val:
        #         return False
        #     return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        
        # return dfs(root, float('-inf'), float('inf'))
        # # t: O(n), s: O(n)
        # ---
        # 2. BFS
        if not root:
            return True
        from collections import deque

        q = deque()
        q.append((root, float('-inf'), float('inf')))

        while q:
            node, low, high = q.popleft()
            
            if not low < node.val < high:
                return False
            if node.left:
                q.append((node.left, low, node.val))
            if node.right:
                q.append((node.right, node.val, high))

        return True
            

            

        
        