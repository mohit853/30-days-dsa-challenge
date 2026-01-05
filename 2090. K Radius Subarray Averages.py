class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:


        n= len(nums)
        avgs = [-1]*n

        window_size = (2*k) +1

        if window_size > n:
            return avgs

        prefix_sum = [0] * (n + 1)
        for i in range(1,n+1):


            prefix_sum[i] = nums[i-1] + prefix_sum[i-1]

        for i in range(k,n-k):

            
            curr_sum = prefix_sum[i+k+1] - prefix_sum[i-k]

            avgs[i]=(curr_sum) // window_size

        return avgs
        
