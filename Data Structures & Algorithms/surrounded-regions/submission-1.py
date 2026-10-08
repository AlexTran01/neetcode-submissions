class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def bfs(r, c):

            if (r == -1 or r == ROWS or c == -1 or c == COLS or
            board[r][c] == "X" or
            board[r][c] == "T"):
                return 

            board[r][c] = "T"

            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)

        for c in range(COLS):
           bfs(0, c)
           bfs(ROWS-1, c)

        for r in range(ROWS):
           bfs(r, 0)
           bfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        
