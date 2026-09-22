class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            k = (lo + hi) // 2
            eat_time = 0
            for x in piles:
                eat_time += (x + k - 1) // k
            if eat_time <= h:
                hi = k
            else:
                lo = k + 1
        return lo

        