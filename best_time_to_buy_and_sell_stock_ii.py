class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit =0
        buy = prices[0]
        n=len(prices)

        for i in range(1,n):
            sell = prices[i]

            if sell > buy:
                profit += sell -buy
            buy = prices[i]
        
        return profit
        
