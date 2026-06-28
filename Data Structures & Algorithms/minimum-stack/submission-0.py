class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.Min or val < self.Min[-1]:
            self.Min.append(val)
        else:
            self.Min.append(self.Min[-1])
        return None

    def pop(self) -> None:
        self.Min.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1] if self.Min else None


        
