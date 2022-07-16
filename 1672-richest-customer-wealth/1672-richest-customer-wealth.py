class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            max_wealth = max(max_wealth,wealth)
        return max_wealth
            
        