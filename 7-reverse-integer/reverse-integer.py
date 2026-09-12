class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x != 0:
            res = res * 10 + (x % 10)
            x //= 10
            
        res *= sign
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
