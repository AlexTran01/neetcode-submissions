class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnHashs = [defaultdict(int) for i in range(9)]
        boxHashs = [defaultdict(int) for i in range(3)]

        for i in range(9):

            rowHash = defaultdict(int)

            if(i % 3 == 0):
                boxHashs = [defaultdict(int) for i in range(3)]

            for j in range(9):
                num = board[i][j]

                if(num == "."):
                    continue

                if(rowHash[num] ):
                    return False
                
                if (columnHashs[j][num]):
                    return False
                
                if (boxHashs[j // 3][num]): # it is the column index that tell you what box position
                    return False

                rowHash[num] = 1
                columnHashs[j][num] = 1
                boxHashs[j // 3][num] = 1
        
        return True   