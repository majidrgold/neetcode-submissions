class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## 1. BRUTE FORCE
        res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == "(" else -1  
                if open < 0:
                    return False
            
            return not open
        
        def dfs(s: str):
            if len(s) == n * 2:
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + "(")
            dfs(s + ")")
        
        dfs("")
        return res
        # # t: O()?
        ## 2. Backtrack



        