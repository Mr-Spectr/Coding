class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            good_int = str(i) * 3
            if good_int in num:
                return good_int
        
        return ""

