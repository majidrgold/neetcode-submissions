class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #   return sorted(s) == sorted(t)
    #   # t:[nlogn] s: [n]  
        count = dict()
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] = count.get(c, 0) - 1

        for c in count:
            if count[c] != 0:
                return False

        return True
        # t:[O(n)] s:[O(n+m)]
