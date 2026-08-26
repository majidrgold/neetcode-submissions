class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        for st in s:
            hash_s[st] = hash_s.get(st, 0) + 1
        for st in t:
            if (st in hash_s) and (hash_s[st] > 0):
                hash_s[st] -= 1
            else:
                return False
        return True 

        