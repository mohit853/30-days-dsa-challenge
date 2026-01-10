class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        ##  2  grps majority(M) and non majortiy(R)

        ## M > R 

        ## if only count of  M (M+1) >= count of R
        ## for alteast m+1 we don't need (count of m == count of R) we care +x

        ## we asssume first element is M and update if we find other 
        win_count = 0
        ans = nums[0]
        n= len(nums)
        for num in nums:

            if win_count ==0 :
                ans = num
            
            if num ==  ans:
                win_count +=1
            else:
                win_count -=1 ## nullify 
        return ans


        
