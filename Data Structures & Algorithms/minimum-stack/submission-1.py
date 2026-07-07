class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.len = 0
    
    def push(self, val: int):
        if self.len == 0: 
            self.stack.append(val)
            self.minStack.append(val)
        else: 
            self.stack.append(val)
            self.minStack.append(min(self.minStack[-1], val))

        self.len += 1

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
        self.len -= 1
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]