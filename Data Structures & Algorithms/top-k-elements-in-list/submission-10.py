class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1 - Counter and search
        # from collections import Counter
        # counts = Counter(nums)

        # return sorted(counts, key=counts.get, reverse=True)[:k]
        # # t: [nlogn] s:[O(n)]
        # 2. Min-heap
        import heapq
        counts = Counter(nums)
        res = []
        for num in counts:
            heapq.heappush(res, (counts[num], num))
            if len(res) > k:
                heapq.heappop(res)

        return  [n[1] for n in res]       