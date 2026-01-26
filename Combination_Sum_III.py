class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        results=[]
        ## 3 start_num , current_path , current_sum
        def backtrack(start_num,current_path, current_sum):
            if current_sum == n and len(current_path) == k:
                results.append(current_path.copy())
                return

            if len(current_path)== k  or current_sum ==n:
                return
            
            for i in range(start_num,10):

                current_path.append(i)
                backtrack(i+1, current_path, current_sum +i)
                current_path.pop()


        
        
        backtrack(1, [], 0)
        

        return results
