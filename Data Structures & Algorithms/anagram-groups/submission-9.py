from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 

        res = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            res[key].append(word)
        
        return list(res.values())
        # O(m * nlogn) o(m * n)
        # # 2. using key
        # res = defaultdict(list)

        # def get_key(s):
        #     key = [0] * 26
        #     for c in s:
        #         key[ord(c) - ord('a')] += 1
        #     return tuple(key)

        # for s in strs:
        #     key = get_key(s)
        #     res[key].append(s)
        
        # return list(res.values())
        # # O(m * n), O(m * n) m: number of strings in strs, n: length of longest string

