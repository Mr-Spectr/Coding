class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0

        for account in accounts:
            money_sum=0
            for money in account:
                money_sum+=money
            if money_sum>max_wealth:
                max_wealth=money_sum
        return max_wealth