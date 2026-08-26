# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1. DFS - By me
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res

        # ---
        # 2.0 BFS - By me
        # from collections import deque

        # if not root:
        #     return []

        # res = []
        # q = deque([root])
        
        # while q:
        #     len_level = len(q)
        #     cur_level = []
        #     for _ in range(len_level):
        #         node = q.popleft()
        #         cur_level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(cur_level)
        
        # output = [ele[-1] for ele in res]
        # return output
        # # t: O(n), s: O(n)
        # ---
        # # 2. Optimized BFS
        # from collections import deque

        # if not root:
        #     return []

        # res = []
        # q = deque([root])
        
        # while q:
        #     len_level = len(q)
        #     right_side = None
        #     for _ in range(len_level):
        #         node = q.popleft()
        #         if node:
        #             right_side = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if right_side:
        #         res.append(right_side.val)
        
        # return res
        # # t: O(n), s:O(n)