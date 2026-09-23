class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # up : row -1
        # down: row + 1
        # right: col + 1
        # left: col - 1

        checked = set() # (r,c)
        res = 0

        def backtrack(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == "0" or (r,c) in checked:
                return
            
            checked.add((r, c))
            print(r,c)
            backtrack(r-1, c)
            backtrack(r+1, c)
            backtrack(r, c+1)
            backtrack(r, c-1)
           
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in checked:
                    backtrack(row, col)
                    res += 1
                
        
        return res
