class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        results =[]
        ## total_length =k
        ## chose from 1 to n

        def backtrack(start_num , curr_path, length):

            
            if length == k :
                results.append(curr_path.copy())
                return

            for i in range(start_num,n+1):
                
                curr_path.append(i)
                backtrack(i+1, curr_path,length+1)
                curr_path.pop()
                




        backtrack(1,[],0)
        return results
