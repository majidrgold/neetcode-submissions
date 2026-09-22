class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # 1. 
        # from collections import defaultdict

        # res = defaultdict(list)

        # for s in strs:
        #     key = ''.join(sorted(s))
        #     res[key].append(s)
        
        # return list(res.values())
        # # O(nlogn) o(n)
        # 2. using key
        from collections import defaultdict

        res = defaultdict(list)

        def get_key(s):
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            return tuple(key)

        for s in strs:
            key = get_key(s)
            res[key].append(s)
        
        return list(res.values())

