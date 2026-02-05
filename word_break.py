class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        n= len(s)
        dp = [False]*(n+1)
        ## base case  empty string is T
        dp[0] = True

        for i in range(1,n+1):
            for j in range(i):

                if dp[j]  and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[n]
                     
        
