class MinStack:

    def __init__(self):
        self.stack = deque()
        self.track = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.track and val >= self.track[-1]:
            self.track.append(self.track[-1])
        else:
            self.track.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.track.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.track[-1]
        
