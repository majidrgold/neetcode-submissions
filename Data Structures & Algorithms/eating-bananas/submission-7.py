class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        def count_hour(piles, m):
            return sum((pile + m - 1) // m for pile in piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if count_hour(piles, mid) <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo

sol = Solution()
print((sol.minEatingSpeed(piles = [1,4,3,2], h = 9)))
# 2
print((sol.minEatingSpeed(piles = [25,10,23,4], h = 4)))
# 25

