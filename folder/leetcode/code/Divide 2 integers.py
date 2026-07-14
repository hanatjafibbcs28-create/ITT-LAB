class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0 or dividend == -2**31 and divisor == -1:
            return (2**31) - 1
        # if dividend == -2**31 and divisor == -1:
        #     return (2**31) - 1
        res = abs(dividend) // abs(divisor)
        if (dividend < 0) ^ (divisor < 0):
            return -res
        else:
            return res 
