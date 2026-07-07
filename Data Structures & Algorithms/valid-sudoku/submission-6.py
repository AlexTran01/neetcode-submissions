class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set) # key = (r // 3 ,c // 3)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if( num in row[i] or 
                   num in col[j] or
                   num in box[(i //3, j//3)]):
                    return False

                row[i].add(num)
                col[j].add(num)
                box[((i //3, j//3))].add(num)
        return True
