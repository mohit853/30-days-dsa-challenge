class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ### main logic 3*3 matrix 
        ## base case 1 , only 1 row 
        ## base case 2 , only 1 col

        rows = len(matrix)
        cols = len(matrix[0])

        left =0 
        top =0
        right= cols-1
        bottom = rows-1
        res=[]
        while  left<= right and  top<=bottom:

            ## left to right
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1

            ## top to bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            ## right to left
            if top <= bottom:
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom-=1

            ## bottom to top

            if left <= right:
                for i in  range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1

        return res



        
       



