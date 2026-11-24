class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # sort:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        # O(nlogn), O(1)
        # # counter
        # if len(s) != len(t):
        #     return False
        # counts = {}
        # for c in s:
        #     counts[c] = counts.get(c, 0) + 1
        # for c in t:
        #     if counts.get(c, 0) > 0:
        #         counts[c] -= 1
        #     else:
        #         return False
            
        # for c in counts:
        #     if counts[c] != 0:
        #         return False
        
        # return True 
        # O(n), O(n)
        # counter optimised:
        if len(s) != len(t):
            return False
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1
        for c in counts:
            if counts[c] != 0:
                return False
        return True
        # O(n), O(n)
        # # usign list
        # if len(s) != len(t):
        #     return False
        # counts = [0] * 26
        # for i in range(len(s)):
        #     counts[ord(s[i]) - ord('a')] += 1
        #     counts[ord(t[i]) - ord('a')] -= 1

        # return all(v==0 for v in counts)
        # # O(n), O(n)






