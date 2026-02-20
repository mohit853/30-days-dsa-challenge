class Solution:
    def totalNQueens(self, n: int) -> int:
        
        col_set = set()   

        pos_diag = set()  

        neg_diag = set ()  
        self.count =0
        def backtrack(r):
            if r == n:
                self.count+=1
                return 
            
            for c in range(n):
                if c in col_set or (r+c) in pos_diag or (r-c) in neg_diag :
                    continue
                
                col_set.add(c)
                pos_diag.add(r+c) 
                neg_diag.add(r-c)

                backtrack(r+1)

                col_set.remove(c)
                pos_diag.remove(r+c) 
                neg_diag.remove(r-c)
    
        backtrack(0)

        return self.count
