class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. BruteForce
        if not t or len(s) < len(t):
            return ""
        
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        res = [-1, -1]
        res_len = float("inf")

        for i in range(len(s)):
            count_cur = {}
            for j in range(i, len(s)):
                count_cur[s[j]] = count_cur.get(s[j], 0) + 1

                state = True
                for c in count_t:
                    if count_cur.get(c, 0) < count_t[c]:
                        state = False
                        break
                    
                
                if state and (j - i + 1) < res_len:
                    res = [i, j]
                    res_len = j - i + 1
        l, r = res
        if res_len == "inf":
            return ""
        
        return s[l: r + 1]