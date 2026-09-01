class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            left = n // divider
            curr = (n // i) % 10
            right = n % i
            count += left * i
            if curr == 1:
                count += right + 1
            elif curr > 1:
                count += i
            i *= 10
        return count
