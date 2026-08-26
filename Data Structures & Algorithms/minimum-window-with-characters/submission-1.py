class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # 1. BruteForce
        # if not t or len(s) < len(t):
        #     return ""
        
        # count_t = {}
        # for char in t:
        #     count_t[char] = count_t.get(char, 0) + 1

        # res = [-1, -1]
        # res_len = float("inf")

        # for i in range(len(s)):
        #     count_cur = {}
        #     for j in range(i, len(s)):
        #         count_cur[s[j]] = count_cur.get(s[j], 0) + 1

        #         state = True
        #         for c in count_t:
        #             if count_cur.get(c, 0) < count_t[c]:
        #                 state = False
        #                 break
                    
                
        #         if state and (j - i + 1) < res_len:
        #             res = [i, j]
        #             res_len = j - i + 1
        # l, r = res
        # if res_len == "inf":
        #     return ""
        
        # return s[l: r + 1]
        # # t: O(n^2 * m) s: O(m)

        # Sliding Window:
        if t == "" or len(s) < len(t):
            return ""

        count_t , window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            # update window with r char
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # check if changes have cond
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            # shrink form left
            while have == need:
                # update res, res_len
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # update have
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        if res_len == float('inf'):
            return ""
        
        return s[ l: r + 1]





