class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        LESS_THAN_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return LESS_THAN_20[n] + " "
            elif n < 100:
                return TENS[n // 10] + " " + helper(n % 10)
            else:
                return LESS_THAN_20[n // 100] + " Hundred " + helper(n % 100)
        result = ""
        idx = 0
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + THOUSANDS[idx] + " " + result
            num //= 1000
            idx += 1
        return result.strip()
