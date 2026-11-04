class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def cal_key(s):
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
        
            return tuple(key)

        anagrams = {}

        for st in strs:
            curr_key = cal_key(st)
            if curr_key in anagrams:
                anagrams[curr_key].append(st)
            else:
                anagrams[curr_key] = [st]
        
        return list(anagrams.values())
        # t: O(n*m) n: number of strings, m: longest string s: O(n*m)
        