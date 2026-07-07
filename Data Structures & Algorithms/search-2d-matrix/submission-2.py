class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # position: #ele in 1row * i + j
        n, m = len(matrix), len(matrix[0])
        l = 0
        r = n * m -1

        while l <= r:
            mid = l + ((r - l) // 2)
            
            row, col = mid // m, mid % m # *Note*: row = index // number of collumn, col = index % number of collumn
            # print(f"start :=: r : {r}, l ; {l}, mid : {mid}, row : {row}, col : {col}")
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                if col == 0 and row == 0:
                    break
                elif col == 0: 
                    r = (row-1) * m + m - 1
                else: 
                    r = row * m + (col - 1)
            else: 
                if col == m and row == n:
                    break
                elif col == m:
                    l = (row+1) * m
                else: 
                    l = row * m + (col + 1)
            # print(f"r : {r}, l ; {l}, mid : {mid}, row : {row}, col : {col} \n")
        return False