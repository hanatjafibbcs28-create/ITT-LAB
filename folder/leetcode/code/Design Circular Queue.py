class MyCircularQueue:
    def __init__(self, k: int):
        self.nums = [0] * k
        self.numElements = 0
        self.start = 0
        self.end = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.nums[self.end] = value
        self.end = (1 + self.end) % len(self.nums)
        self.numElements += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % len(self.nums)
        self.numElements -= 1
        return True
    def Front(self) -> int:
        return -1 if self.numElements == 0 else self.nums[self.start]
    def Rear(self) -> int:
        return -1 if self.numElements == 0 else self.nums[(self.end - 1) % len(self.nums)]
    def isEmpty(self) -> bool:
        return self.numElements == 0
    def isFull(self) -> bool:
        return self.numElements == len(self.nums)
    def resize(self):
        newNums = [0] * (2 * len(self.nums))
        i = 0
        j = self.start
        while j != self.end:
            newNums[i] = self.nums[j]
            i += 1
            j = (j + 1) % len(self.nums)
        self.start = 0
        self.end = self.numElements
        self.nums = newNums
