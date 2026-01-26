class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        results = []

        def backtrack(start_idx,curr_path,curr_sum):

            if curr_sum == target :
                results.append(curr_path.copy())
                return


            for i in range(start_idx,len(candidates)):
                
                if curr_sum + candidates[i] > target:
                    continue
                
                num = candidates[i]
                
                curr_path.append(num)
                backtrack(i,curr_path, curr_sum + num)
                curr_path.pop()

            

        backtrack(0,[],0)
        return results
