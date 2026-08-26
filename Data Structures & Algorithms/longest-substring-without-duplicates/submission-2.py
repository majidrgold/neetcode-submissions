class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 2. Sliding Window
        # res = 0
        # l = 0
        # char_set = set()

        # for r in range(len(s)):
        #     while s[r] in char_set:
        #         char_set.remove(s[l])
        #         l += 1
        #     char_set.add(s[r])
        #     res = max(r - l + 1, res)
        
        # return res
        # # t: O(n), s: O(m)

        # 3. Sliding Window (Optimal)
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        
        return res




        