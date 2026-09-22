class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = {}
        for char in s:
            s_counter[char] = s_counter.get(char, 0) + 1
        
        for char in t:
            if char not in s_counter:
                return False
            s_counter[char] -= 1
        
        for v in s_counter.values():
            if v!= 0:
                return False
        
        return True

        # O(n), O(n)

        