class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. counter for each add to that key return that one
        # O(n mlogm) m longest string and n numebr of strings
        # counter = {}
        # for st in strs:
        #     s = tuple(sorted(st))
        #     if s in counter:
        #         lst = counter[s]
        #         lst.append(st)
        #         counter[s] = lst
        #     else:
        #         counter[s] = [st]
        
        # return list(counter.values())
        # 2. hash table
        from collections import defaultdict
        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())    

        


        
        