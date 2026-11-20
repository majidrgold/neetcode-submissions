class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal_hour(k):
            res = 0
            for pile in piles:
                res += (pile - 1) // k + 1
            return res

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (hi + lo) // 2
            if cal_hour(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        
        return lo