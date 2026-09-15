class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        indexed_edges = [e + [i] for i, e in enumerate(edges)]
        weight_map = {}
        for u, v, w, i in indexed_edges:
            if w not in weight_map:
                weight_map[w] = []
            weight_map[w].append((u, v, i))
        parent = list(range(n))
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        critical, pseudo = [], []
        for w in sorted(weight_map.keys()):
            edges_in_layer = weight_map[w]
            local_graph = {}
            edge_list = []
            for u, v, idx in edges_in_layer:
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    if root_u not in local_graph: local_graph[root_u] = []
                    if root_v not in local_graph: local_graph[root_v] = []
                    local_graph[root_u].append((root_v, idx))
                    local_graph[root_v].append((root_u, idx))
                    edge_list.append(idx)
            visited = {}
            ids = {}
            low = {}
            time_tracker = [0]
            bridges = set()
            def dfs(node, parent_edge):
                visited[node] = True
                ids[node] = low[node] = time_tracker[0]
                time_tracker[0] += 1
                for neighbor, edge_idx in local_graph[node]:
                    if edge_idx == parent_edge:
                        continue
                    if neighbor not in visited:
                        dfs(neighbor, edge_idx)
                        low[node] = min(low[node], low[neighbor])
                        if low[neighbor] > ids[node]:
                            bridges.add(edge_idx)
                    else:
                        low[node] = min(low[node], ids[neighbor])
            for node in local_graph:
                if node not in visited:
                    dfs(node, -1)
            for idx in edge_list:
                if idx in bridges:
                    critical.append(idx)
                else:
                    pseudo.append(idx)
            for u, v, idx in edges_in_layer:
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    parent[root_u] = root_v
        return [critical, pseudo]
