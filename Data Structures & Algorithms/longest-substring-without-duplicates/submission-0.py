class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_subst = 0
        l, r = 0, 0
        subst = set()
        "abcabcbb"
        while r < len(s):
            if s[r] in subst:
                subst.remove(s[l])
                l += 1
            else:
                subst.add(s[r])
                r += 1

            max_subst = max((r - l), max_subst)
        
        return max_subst
        