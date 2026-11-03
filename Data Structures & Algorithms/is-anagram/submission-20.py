class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #   return sorted(s) == sorted(t)
    #   # t:[nlogn] s: [n] 
        # if len(s)!= len(t):
        #     return False 
        # count = dict()
        # for c in s:
        #     count[c] = count.get(c, 0) + 1
        # for c  in t:
        #     if count.get(c, 0) == 0:
        #         return False
        #     count[c] -= 1

        # return True
        # # t:[O(n+m)] s:[O(k)]
        # from collections import Counter
        # return Counter(s) == Counter(t)
        # # t:[O(n+m)], s:[O(k)]
        if len(s)!= len(t):
            return False 
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            char = ord(c) - ord('a')
            if count[char] == 0:
                return False
            count[char] -= 1

        return True
        # t:[O(n+m)] s:[O(k)]