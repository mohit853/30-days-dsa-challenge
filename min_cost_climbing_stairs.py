class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        dp =[0]*(n+1)


        ## top down approach , suppose we are at n , we either pay cost[n-1] or cost[n-2] to reach n
        ## base case 
        dp[0]=0
        dp[1]=0

        for i in range(2,n+1):
            

            dp[i] = min(dp[i-1]+ cost[i-1], dp[i-2]+ cost[i-2])


        return dp[n]
