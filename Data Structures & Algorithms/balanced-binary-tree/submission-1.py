# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 1. dfs
        # def dfs(root):
        #     if not root:
        #         return [True, 0]
            
        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(right[1] - left[1]) <= 1
        #     height = 1 + max(left[1], right[1])

        #     return [balanced, height]
        
        # return dfs(root)[0]
        # t: O(n), s: O(n)

        # 2. Iterative DFS
        stack = []
        node = root
        last = None
        depths = {}
        # post order --> left right node
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False
                    
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        
        return True
        # t: O(n), s:O(n)




        

        