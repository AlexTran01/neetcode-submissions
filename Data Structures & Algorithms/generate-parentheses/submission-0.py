class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add open parathensis if open< n
        # only add a closing parathesis if closed < open
        # valid IIF open == Closed ==n

        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res
            