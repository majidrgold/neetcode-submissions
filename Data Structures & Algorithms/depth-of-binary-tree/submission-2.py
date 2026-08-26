# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # 1. DFS - Recursive
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # # t: O(n), s: O(h) (O(logn) to O(n))
        # # 2. DFS - Iterative Stack
        # if not root:
        #     return 0
        # stack = [(root, 1)]
        # max_d = 0
        # while stack:
        #     node, depth = stack.pop()
        #     max_d = max(max_d, depth)
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        
        # return max_d
        # # t: O(n), s: O(n)
        # ---
        # 3. BFS
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level
        # t: O(n), s: O(n)

            



        