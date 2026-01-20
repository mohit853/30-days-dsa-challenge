class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows,cols = len(obstacleGrid) , len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] =1

        for row in range(rows) :
            for col in range(cols) :

                if row ==0 and col ==0:
                    continue

                if obstacleGrid[row][col] == 1:
                    dp[row][col] =0
                else:
                    path_from_left = dp[row][col-1] if col>0 else 0
                    path_from_top = dp[row-1][col] if row>0 else 0
                    dp[row][col] = path_from_left + path_from_top


        return dp[rows-1][cols-1]
