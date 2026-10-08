class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()
        
        def dfs(row, col, ocean, prevHeight):
            if (row == -1  or row == ROWS or col == -1 or col == COLS or 
            (row, col) in ocean or 
            prevHeight > heights[row][col]):
                return
            
            ocean.add((row,col))

            dfs(row - 1 , col, ocean, heights[row][col])
            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

                

            

        