# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.stack = []
        self._push_all_left(root)
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_all_left(node.right)
        return node.val
    def hasNext(self) -> bool:
        return len(self.stack) > 0
    def _push_all_left(self, node: TreeNode | None) -> None:
        while node:
            self.stack.append(node)
            node = node.left
