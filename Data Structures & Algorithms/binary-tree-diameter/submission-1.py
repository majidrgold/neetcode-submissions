# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # # 1. dfs
        # res = 0
        # def dfs(root):
        #     nonlocal res

        #     if not root:
        #         return 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     res = max(res, left + right)
        #     return 1 + max(left, right)
        
        # dfs(root)
        # return res
        # # t: O(n), s: O(n)
        # ---
        # 2. iterative DFS        
        stack = [root]
        # mp (node: (h, d))
        mp = {None: (0, 0)}
        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_h, left_d = mp[node.left]
                right_h, right_d = mp[node.right]

                mp[node] = (1 + max(left_h, right_h),
                            max(left_h + right_h, left_d, right_d))

        return mp[root][1]


