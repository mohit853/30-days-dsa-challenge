class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## 2 base cases 
        ## [2,8]
        ## [2]

        profit =0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price,price)

            profit = max(profit, price-min_price)
        
        return profit
