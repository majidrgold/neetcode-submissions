class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # 1. my try - reverse
        # s = ''.join(c.lower() for c in s if c.isalnum())
        # print(s)
        # return s == s[::-1]
        # # t: O(n), s:O(n)
        # ---
        # # 2. Two pointer - my solution
        s = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
        # # t: O(n) s: O(n)
        # # ---
        # # 3. 2 pointers without cleaning
        # l, r = 0, len(s) - 1

        # while l < r
            
