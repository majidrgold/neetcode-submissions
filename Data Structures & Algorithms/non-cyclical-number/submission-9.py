class Solution:
    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output

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
        # # 2. Fast and Slow Pointers - Floyd's algo
        # def sumOfSquares(n: int) -> int:
        #     output = 0
        #     while n:
        #         digit = n % 10
        #         output += digit ** 2
        #         n = n // 10
            
        #     return output
        
        # slow = n
        # fast = sumOfSquares(n)

        # while fast != 1 and slow != fast:
        #     slow = sumOfSquares(slow)
        #     fast = sumOfSquares(sumOfSquares(fast))
        
        # return fast == 1
        # # O(logn), O(1)
        # 3. Fast And Slow Pointers - II - Brent's algo
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1
        while fast !=1 and slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            
            fast = self.sumOfSquares(fast)
            lam += 1
        
        return fast == 1








        