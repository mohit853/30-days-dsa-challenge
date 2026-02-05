class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n= len(nums)
        dp = [1]*(n)

      
        max_i = 1
        for i in range(n):
            for j in range(i):

                if nums[i] > nums[j] and 1+ dp[j] > dp[i]:
                    dp[i] = 1+ dp[j]
                
         
        return max(dp)
                    
