class Solution:
    def isHappy(self, n: int) -> bool:
        # # 1. Hash set
        # def sum_digit(n):
        #     return sum([int(d) ** 2 for d in str(n)])
        
        # seen = set()
        # while n != 1:
        #     if n in seen:
        #         return False
        #     seen.add(n)
        #     n = sum_digit(n)
        
        # return True
        # # O(logn), O(logn)
        # 2. Fast and Slow Pointers 
        def sumOfSquares(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output
        
        slow = n
        fast = sumOfSquares(n)

        while fast != 1 and slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        
        return fast == 1






        