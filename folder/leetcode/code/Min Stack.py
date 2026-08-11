class MinStack(object):
    def __init__(self): self.s, self.m = [], []
    def push(self, x): self.s.append(x); (not self.m or x <= self.m[-1]) and self.m.append(x)
    def pop(self): self.s.pop() == self.m[-1] and self.m.pop()
    def top(self): return self.s[-1]
    def getMin(self): return self.m[-1]
