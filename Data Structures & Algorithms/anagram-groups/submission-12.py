class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        base = ord('a')

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - base] += 1
            groups[tuple(counts)].append(s)
        
        return list(groups.values())
