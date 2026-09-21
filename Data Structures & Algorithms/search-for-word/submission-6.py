class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # right: col + 1
        # left: col - 1 
        # up: row - 1
        # down : row -1 
        usedPost = defaultdict(int)

        def backtrack(r, c, w):
            if not w:
                return True
                
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or usedPost[(r,c)]:
                return False

            if board[r][c] == w[0]:
                usedPost[(r,c)] = 1
               
                val = (True and 
                (backtrack(r, c+1, w[1:]) or 
                backtrack(r, c-1, w[1:]) or 
                backtrack(r-1, c, w[1:]) or 
                backtrack(r+1, c, w[1:])))

                usedPost.pop((r,c))
                
                return val
                
            return False
    

        for row in range(len(board)):
            for col in range(len(board[0])):
                print(board[row][col])
                if board[row][col] == word[0]:
                    # start looking
                    if backtrack(row, col, word):
                        return True
                    
        return False