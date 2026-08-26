# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. DFS
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        return res
        # t: O(n), s: O(n)

        # ---
        # # 2. BFS
        # from collections import deque
        # if not root:
        #     return []

        # queue = deque([root])
        # res = []
        # while queue:
        #     level_size = len(queue)
        #     cur_level = []
        #     for _ in range(level_size):
        #         node = queue.popleft()                    
        #         cur_level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(cur_level)
        
        # return res
        # # t: O(n), s: O(n)
        # ---
        # 
        