class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        
        return list(res.values())
        # O(nlogn) o(n)