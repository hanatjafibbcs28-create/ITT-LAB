class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        result = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # 4. Overflow check before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
