class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_time(k, piles):
            return sum((pile + k - 1)// k for pile in piles)

        lo, hi = 1, max(piles)

        while lo < hi:
            k = (lo + hi) // 2

            if eat_time(k, piles) <= h:
                hi = k
            else:
                lo = k + 1
        return lo

        