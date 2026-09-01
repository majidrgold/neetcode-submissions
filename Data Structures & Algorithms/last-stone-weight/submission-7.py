class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sorting
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if len(stones) == 1 else 0
        # t: O(n^2 * log(n)), s: O(1)
        # 1. Binary Search

        # 2. MAX HEAP

        