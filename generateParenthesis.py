class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        
        
        max_len = 2*n
        res = []
        def recursive(curr_str, open_cnt , close_cnt):
            
            if len(curr_str)  == max_len:
                res.append(curr_str)
                return
            
            if open_cnt < n:
                recursive(curr_str + '(', open_cnt+1 , close_cnt )
            
            if close_cnt < open_cnt:
                recursive(curr_str + ')' , open_cnt ,close_cnt+1)
            
            
        
        
        
        
        recursive("", 0 , 0)
        
        return res
