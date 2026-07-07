class Solution:
    def isValid(self, s: str) -> bool:
        # valid only when brackets are open-closed in correct order
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            elif c == ']' or c == '}' or c == ')':
                if not stack:
                    return False
                num = stack.pop()
                if c == ']' and num != '[':
                    return False
                if c == ')' and num != '(':
                    return False
                if c == '}'and num != '{':
                    return False
            else:
                continue

        return True if not stack else False
        