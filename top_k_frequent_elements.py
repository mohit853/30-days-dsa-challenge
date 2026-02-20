class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_nums ={}
        
        for num in nums:
            if num not in hash_nums:
                hash_nums[num] = 1
            else:
                hash_nums[num]  += 1
        
        
        n = len(nums)
        bucket =[[] for _ in range(n+1)]
        
        
        for num , freq in hash_nums.items():
            bucket[freq].append(num)
        
        res =[]
        
        
        for i in range(n, -1 , -1):
            for n in bucket[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
            
            
            
                
