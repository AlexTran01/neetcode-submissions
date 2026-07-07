class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                if len(stack) < 2:
                    return -1
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum + firstNum)

            elif token == "-":
                if len(stack) < 2:
                    return -200
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum - firstNum)

            elif token == "*":
                if len(stack) < 2:
                    return -200
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum * firstNum)

            elif token == "/":
                if len(stack) < 2:
                    return -200
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(int(secondNum / firstNum))

            else:## token is a number by constrains
                stack.append(int(token))

        return stack.pop()