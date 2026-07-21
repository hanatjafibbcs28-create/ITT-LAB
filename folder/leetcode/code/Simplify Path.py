class Solution:
    def simplifyPath(self, path: str) -> str:
        segments = path.split('/')
        stack = []
        for segment in segments:
            if not segment or segment == '.':
                continue
            if segment == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(segment)
        return '/' + '/'.join(stack)
