class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # counts = Counter(nums)
        
        # return sorted(counter, key=lambda x: x for x in counter.values)[:k]
        # # t: O(nlogn), s: O(n)
        import heapq
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []

        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = [heapq.heappop(heap)[1] for i in range(k)]
        return res



        