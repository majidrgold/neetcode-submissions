class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. Brute Force
        n = len(heights)
        max_h = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_h = max(max_h, min(heights[j], heights[i]) * (j - i))
        return max_h
        