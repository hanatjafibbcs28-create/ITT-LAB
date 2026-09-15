class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.state = 123456789
        self.mod = 2**31 - 1
        self.mult = 1103515245
        self.inc = 12345
    def _next_uniform(self) -> float:
        self.state = (self.mult * self.state + self.inc) % self.mod
        return self.state / self.mod
    def randPoint(self) -> list[float]:
        diameter = 2 * self.radius
        while True:
            x_offset = (self._next_uniform() * diameter) - self.radius
            y_offset = (self._next_uniform() * diameter) - self.radius
            if (x_offset * x_offset) + (y_offset * y_offset) <= self.radius * self.radius:
                return [self.x_center + x_offset, self.y_center + y_offset]
