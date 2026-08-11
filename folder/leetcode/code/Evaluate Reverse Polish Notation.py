from collections import deque
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        q = deque()
        right = None
        for x in tokens:
            if x not in "+-*/":
                q.append(int(x))
            else:
                right = q.pop()
                left = q.pop()
                if x == "+":
                    q.append(left + right)
                if x == "-":
                    q.append(left - right)
                if x == "*":
                    q.append(left * right)
                if x == "/":
                    q.append(int(left / right))
        return q[0]
