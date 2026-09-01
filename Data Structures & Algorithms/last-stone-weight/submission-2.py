class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                diff = stones[-1] - stones[-2]
                stones = stones[:-2]
                stones.append(diff)

        return stones[0] if len(stones) == 1 else 0
        