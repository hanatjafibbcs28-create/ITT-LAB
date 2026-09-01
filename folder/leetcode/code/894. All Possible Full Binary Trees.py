class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        if n % 2 == 0:
            return []
        memo = {}
        def generate_trees(num_nodes: int) -> list[TreeNode]:
            if num_nodes == 1:
                return [TreeNode(0)]
            if num_nodes in memo:
                return memo[num_nodes]
            res = []
            for left_size in range(1, num_nodes - 1, 2):
                right_size = num_nodes - 1 - left_size
                left_subtrees = generate_trees(left_size)
                right_subtrees = generate_trees(right_size)
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        res.append(root)
            memo[num_nodes] = res
            return res
        return generate_trees(n)
