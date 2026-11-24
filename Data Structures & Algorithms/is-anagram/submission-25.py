class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # sort:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        # O(nlogn), O(1)
        # counter
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            if counts.get(c, 0) > 0:
                counts[c] -= 1
            else:
                return False
            
        for c in counts:
            if counts[c] != 0:
                return False
        
        return True 

