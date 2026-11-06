class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 - Counter and search
        from collections import Counter
        counts = Counter(nums)

        return sorted(counts, key=counts.get, reverse=True)[:k]
        