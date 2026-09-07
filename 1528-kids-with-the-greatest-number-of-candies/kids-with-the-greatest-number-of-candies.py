class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_val = max(candies)
        return [candy + extraCandies >= max_val for candy in candies]
