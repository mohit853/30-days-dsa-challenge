class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col_zero = False
        row_zero = False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            if matrix[i][0] ==0 :
                col_zero = True
        
        
        for j in range(cols):
            if matrix[0][j] ==0 :
                row_zero = True
        
        
        for i in range(1,rows):
            for j in range(1,cols):
                
                if matrix[i][j] == 0:
                    matrix[i][0] =0
                    matrix[0][j] =0
        
        ##### second pass #########33
        
        for i in range(1,rows):
            for j in range(1,cols):
                
                ## make whole col to -
                if matrix[i][0] == 0 or matrix[0][j]  == 0:
                    matrix[i][j] =0
        if row_zero:
            for j in range(cols):
                matrix[0][j] =0
        
        if col_zero:
            for i in range(rows):
                matrix[i][0] =0
    
                
                
        
        
