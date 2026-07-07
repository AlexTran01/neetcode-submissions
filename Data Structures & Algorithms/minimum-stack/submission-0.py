class MinStack:

  
    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self, val: int):
        self.stack.append(val)
        self.len += 1

    def pop(self):
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return min(self.stack)
        
