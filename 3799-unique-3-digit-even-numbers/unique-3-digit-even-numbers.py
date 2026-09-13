from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        available = Counter(digits)
        ans = 0
        
        for num in range(100, 1000):
            if num % 2 != 0:
                continue
                
            s = str(num)
            needed = Counter(s)
            
            possible = True
            for digit, count in needed.items():
                if available[int(digit)] < count:
                    possible = False
                    break
            
            if possible:
                ans += 1
                
        return ans
