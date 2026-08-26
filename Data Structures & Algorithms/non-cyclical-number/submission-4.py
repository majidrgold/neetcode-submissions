class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_digit(n):
            return sum([int(d) ** 2 for d in str(n)])
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_digit(n)
        
        return True



        