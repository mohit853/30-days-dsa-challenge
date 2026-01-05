class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

    ## design of window : assume window size is fixed lets say 4 in list of 6 , it would be our result if it had atmost k zeroes  

    ## window can be of any size not fixed 

        left =0
        right = 0
        n= len(nums)
        max_len = 0
        cnt_zeroes=0
        for right in range(n):

            if nums[right] == 0:
                cnt_zeroes +=1
            
            while cnt_zeroes >k:
                if nums[left] ==0:
                    
                    cnt_zeroes-=1
                left+=1
            
            max_len = max(max_len, right-left+1)
        return max_len


            


        
