class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## Boottom up
        inf = amount+1
        dp =[inf] * (amount+1)
        ## base case 
        dp[0] =0 

        ## Looping 

        for i in range(1,amount+1):
            for coin in coins:
                
                if i>=coin:
                    dp[i]=min(1+dp[i-coin],dp[i])
        
        res=-1
        if dp[amount] <= amount:
            res=dp[amount]
        return res
    
