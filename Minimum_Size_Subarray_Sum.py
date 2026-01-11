class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len =float('inf')

        i=0
        j=0
        n=len(nums)
        curr_sum=0
        while j<n:
            curr_sum +=nums[j]
        
            while curr_sum >= target:
                
                
                min_len = min(min_len, j-i+1)
                curr_sum -= nums[i]
                i+=1
            j+=1



        return 0 if min_len == float('inf') else  min_len

