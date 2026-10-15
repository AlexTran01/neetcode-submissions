class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        cur = []

        def backtrack(start):

            if len(cur) == k:
                res.append(cur.copy())
                return
            
            if start > n:
                return
            
            
            # pick i
            # for i in range(start, n+1):
            cur.append(start)
            backtrack(start+1)
            cur.pop()

            backtrack(start+1)


        backtrack(1)
        return res

