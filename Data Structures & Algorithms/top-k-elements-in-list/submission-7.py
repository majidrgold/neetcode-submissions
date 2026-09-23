class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # 1. Counter and Sort
    #    from collections import Counter
    #    counts = Counter(nums)
    #    res = sorted(counts, key=counts.get, reverse=True)
    #    return res[:k]
    #    # O(nlogn), O(n)
       # 2. with heap
       import heapq
       from collections import Counter
       counts = Counter(nums)
       return heapq.nlargest(k, counts.keys(), key=counts.get)

