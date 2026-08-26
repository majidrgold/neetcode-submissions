class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # # 3. Sliding Window (Optimal)
        # count = {}
        # l = 0
        # max_freq = 0
        # res = 0

        # for r in range(len(s)):
        #     count[s[r]] = count.get(s[r], 0) + 1
        #     max_freq = max(max_freq, count[s[r]])

        #     while (r - l + 1) - max_freq > k:
        #         count[s[l]] -= 1
        #         l += 1

        #     res = max(res, r - l + 1)

        # return res
        # # t: O(n) s: O(m) - alphabet fixed size
        # ---
        # 2. sliding window
        chars = set(s)
        res = 0

        for c in chars:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c: 
                    count += 1
                    
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res




        