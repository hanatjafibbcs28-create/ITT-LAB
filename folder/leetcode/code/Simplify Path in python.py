class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
        for portion in components:
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or portion == "":continue
            else:
                stack.append(portion)
        return "/" + "/".join(stack)
