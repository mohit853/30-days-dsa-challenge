class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        ## dp as there are sub-problems

        ## 2 states one is possesing stock at end of day 
        ## other is not possesing at end of day


        profit_with_stock = -prices[0]
        profit_without_stock = 0

        for price in prices[1:]:

            profit_without_stock = max(profit_without_stock , profit_with_stock + price - fee)
            profit_with_stock = max(profit_with_stock , profit_without_stock - price)

        return profit_without_stock
