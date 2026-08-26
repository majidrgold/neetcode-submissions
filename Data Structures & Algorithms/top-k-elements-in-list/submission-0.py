class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        return sorted(counter.keys(), key=counter.get, reverse=True)[:k]
        

        