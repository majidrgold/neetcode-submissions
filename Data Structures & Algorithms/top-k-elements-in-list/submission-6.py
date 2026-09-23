class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       from collections import Counter
       counts = Counter(nums)
       res = sorted(counts, key=counts.get, reverse=True)
       return res[:k]
       # O(nlogn), O(n)
