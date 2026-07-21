class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        in_idx = len(inorder) - 1
        for i in range(len(postorder) - 2, -1, -1):
            curr_val = postorder[i]
            node = stack[-1]
            if node.val != inorder[in_idx]:
                node.right = TreeNode(curr_val)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[in_idx]:
                    node = stack.pop()
                    in_idx -= 1   
                node.left = TreeNode(curr_val)
                stack.append(node.left)    
        return root
