class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2. Slidign Window
        res = 0
        l = 0
        char_set = set()
        "abcabcbb"
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(r - l + 1, res)
        
        return res
        