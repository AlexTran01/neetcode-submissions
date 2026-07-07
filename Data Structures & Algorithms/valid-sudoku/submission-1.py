class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnHashs = [set() for i in range(9)]
        boxHashs = [set() for i in range(3)]

        for i in range(9):

            rowHash = set()

            if(i % 3 == 0):
                boxHashs = [set() for i in range(3)]

            for j in range(9):
                num = board[i][j]

                if(num == "."):
                    continue

                if(num in rowHash):
                    return False
                
                if (num in columnHashs[j]):
                    return False
                
                if (num in boxHashs[j // 3]): # it is the column index that tell you what box position
                    return False

                rowHash.add(num)
                columnHashs[j].add(num)
                boxHashs[j // 3].add(num)
        
        return True   