# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        current = root
        while current:
            if current.left:
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
