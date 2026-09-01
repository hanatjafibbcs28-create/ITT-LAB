import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
        k -= 1
        result = []
        for i in range(n - 1, -1, -1):
            block_size = factorials[i]
            idx = k // block_size
            result.append(numbers.pop(idx))
            k %= block_size
        return "".join(result)
