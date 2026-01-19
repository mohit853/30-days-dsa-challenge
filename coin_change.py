class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ## bottom up , for amount we need to check entire coins List
        ## if amount - coin ==0 , amount-coin = ream_amount 

        ## we need to compute from 0 to amount 


        ## base case II amont =6 , coin [1,2,5]
        ## base case III amount = 4 , coin [1,2,5]
        n= amount
        dp = [float('inf')] *(n+1)
        ## base case I amount =0 , coin =[1,2,5]
        dp[0] =0


        for i in range(1,amount+1) :
            for coin in coins:

                if i-coin >=0:
                    ## for min logic think if we have calucalted for coin 1,
                    ##how do we find for 2
                    dp[i] = min(1+dp[i-coin], dp[i])
        

        return dp[n] if dp[n] != float('inf') else -1


        
