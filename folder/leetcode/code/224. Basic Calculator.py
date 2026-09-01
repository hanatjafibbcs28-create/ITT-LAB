class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_result = 0
        sign = 1
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                current_result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                current_result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1
            elif char == ')':
                current_result += sign * num
                num = 0
                current_result *= stack.pop()  
                current_result += stack.pop()  
        return current_result + (sign * num)
