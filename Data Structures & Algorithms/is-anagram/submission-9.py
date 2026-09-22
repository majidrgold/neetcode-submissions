class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26       # assmption: s & t consists of lower case English letters

        for cs, ct in zip(s, t):
            counts[ord(cs) - ord('a')] += 1
            counts[ord(ct) - ord('a')] -= 1

        return all(counts[i]==0 for i in range(26))
        