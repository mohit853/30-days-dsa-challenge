class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp= [[1]*n for _ in range(m)]

        ##  base cases 
        if m==1 and n==0:
            dp[i][j] = 1+ dp[i-1][j]
        if m==0 and n==1:
            dp[i][j]= 1+dp[i][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i-1][j]+ dp[i][j-1]
        
        return dp[m-1][n-1]
