class MyCircularDeque:
    def __init__(self, k: int): self.b, self.k, self.h, self.t, self.s = [0] * k, k, 0, 0, 0
    insertFront = lambda self, v: False if self.isFull() else [self.b.__setitem__((nh := (self.h - 1) % self.k), v), self.__dict__.update({'h': nh, 's': self.s + 1})].append(None) or True
    insertLast = lambda self, v: False if self.isFull() else [self.b.__setitem__(self.t, v), self.__dict__.update({'t': (self.t + 1) % self.k, 's': self.s + 1})].append(None) or True
    deleteFront = lambda self: False if self.isEmpty() else self.__dict__.update({'h': (self.h + 1) % self.k, 's': self.s - 1}) or True
    deleteLast = lambda self: False if self.isEmpty() else self.__dict__.update({'t': (self.t - 1) % self.k, 's': self.s - 1}) or True; getFront = lambda self: -1 if self.isEmpty() else self.b[self.h]; getRear = lambda self: -1 if self.isEmpty() else self.b[(self.t - 1) % self.k]; isEmpty = lambda self: self.s == 0; isFull = lambda self: self.s == self.k
