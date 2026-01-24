class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        total_island=0

        def find_complete_piece(r,c):

            if r<0 or r>=rows or c<0 or c >=cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            find_complete_piece(r,c+1)
            find_complete_piece(r,c-1)
            find_complete_piece(r+1,c)
            find_complete_piece(r-1 , c)

        for r in range(rows) :
            for c in range(cols):
                if grid[r][c] == "1":
                    total_island+=1
                    find_complete_piece(r,c)

        


        return total_island


        
