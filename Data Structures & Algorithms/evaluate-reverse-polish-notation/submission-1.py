class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum - firstNum)

            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "/":
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(int(secondNum / firstNum))

            else:## token is a number by constrains
                stack.append(int(token))

        return stack[0]