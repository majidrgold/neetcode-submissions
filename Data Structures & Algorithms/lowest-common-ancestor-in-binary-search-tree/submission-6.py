# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # # 1. Recursion
        # if not root or not p or not q:
        #     return None
        # if (max(p.val, q.val) < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif (min(p.val, q.val) > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root
        # # t: O(h), s:O(h)
        # ---
        # ---
        # ---
        # 2. iteration
        
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node
        


        
        

            