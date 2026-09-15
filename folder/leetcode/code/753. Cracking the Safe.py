class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(str(i) for i in range(k))
        visited_edges = set()
        circuit = []
        start_node = "0" * (n - 1)
        def dfs(node: str):
            for i in range(k):
                edge = node + str(i)
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    next_node = edge[1:]
                    dfs(next_node)
                    circuit.append(str(i))
        dfs(start_node)
        return "".join(circuit) + start_node
