class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # solution 1
        # if len(s) != len(t):
        #     return False

        # s_counter = {}
        # for char in s:
        #     s_counter[char] = s_counter.get(char, 0) + 1
        
        # for char in t:
        #     if char not in s_counter:
        #         return False
        #     s_counter[char] -= 1
        
        # for v in s_counter.values():
        #     if v!= 0:
        #         return False
        
        # return True

        # # O(n), O(n)
        # solution 2:
        if len(s) != len(t):
            return False
        
        chars = [0] * 26

        for i in range(len(s)):
            ord_s, ord_t = ord(s[i]) - ord('a'), ord(t[i]) - ord('a')
            chars[ord_s] += 1
            chars[ord_t] -= 1
        
        for i in chars:
            if i != 0:
                return False
        
        return True

        