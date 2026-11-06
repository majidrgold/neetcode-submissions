class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 1 - Counter and search
        # from collections import Counter
        # counts = Counter(nums)

        # return sorted(counts, key=counts.get, reverse=True)[:k]
        # # t: [nlogn] s:[O(n)]
        # # 2. Min-heap
        # import heapq
        # counts = Counter(nums)
        # res = []
        # for num in counts:
        #     heapq.heappush(res, (counts[num], num))
        #     if len(res) > k:
        #         heapq.heappop(res)

        # return  [n[1] for n in res]   
        # # t: O(nlogk) s:O(n)
        # Bucket search
        counts = Counter(nums)
        freqs = [[] for i in range(len(nums) + 1)]
        for num, cnt in counts.items():
            freqs[cnt].append(num)
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for freq in freqs[i]:
                res.append(freq)
                if len(res) == k:
                    return res

