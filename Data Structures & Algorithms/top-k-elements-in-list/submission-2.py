class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. sort method
        # counter = {}
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1
        # return sorted(counter, key=counter.get, reverse=True)[:k]
        # # t: O(nlogn), s:n
        # 2. heap
        import heapq
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        # t: O(nlog), s: O(n+k)
