class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]
        
        results= []

        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                results.append(curr_path.copy())
                return 


            for num in nums:

                if num in curr_path :
                    continue
                curr_path.append(num)

                backtrack(curr_path)

                curr_path.pop()

        

        backtrack([])

        return results
