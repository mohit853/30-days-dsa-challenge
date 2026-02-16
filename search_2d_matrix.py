class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        ## start at top right matrix 
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        i = 0 
        j = cols-1
        
        while i < rows and j >=0:
            
            current = matrix[i][j]
            
            if current == target:
                return True
            
            if current > target:
                j-=1
            else:
                i+=1
        return False
                
        
