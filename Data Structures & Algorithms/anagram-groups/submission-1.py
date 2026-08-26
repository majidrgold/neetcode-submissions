class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. counter for each add to that key return that one
        counter = {}
        for st in strs:
            s = tuple(sorted(st))
            if s in counter:
                lst = counter[s]
                lst.append(st)
                counter[s] = lst
            else:
                counter[s] = [st]
        
        return list(counter.values())
        


        
        