class Solution:
    def isValid(self, s: str) -> bool:
        # valid only when brackets are open-closed in correct order
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            elif c == ']':
                if stack.pop() != '[':
                    return False
            elif c == ')':
                if stack.pop() != '(':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
            else:
                continue
            
        return True
        