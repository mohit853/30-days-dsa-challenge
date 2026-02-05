class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)
        

        for i in range(rows-2,-1,-1):
            for j in range(i+1):
                down = triangle[i][j] + triangle[i+1][j]
                diag = triangle[i][j]  + triangle[i+1][j+1]

                triangle[i][j] = min(down,diag)
        return triangle[0][0]
        
