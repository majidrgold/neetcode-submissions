class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # 1. Brute Force
        # n = len(heights)
        # max_h = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         max_h = max(max_h, min(heights[j], heights[i]) * (j - i))
        # return max_h
        # # t: O(n^2), s=O(1)
        # # ---
        # 2. Tow pointers
        n = len(heights)
        l, r = 0, n - 1
        max_h = 0
        while l < r:
            h = min(heights[l], heights[r])
            cur_h = h * (r - l)
            max_h = max(max_h, cur_h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_h

        
        