class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sum =0 
        res=[]
        for num in nums:
            sum +=num
            res.append(sum)
        return res
