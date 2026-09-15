class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        ids = [-1] * n
        low = [-1] * n
        critical = []
        time_tracker = [0]
        def dfs(u, parent):
            ids[u] = low[u] = time_tracker[0]
            time_tracker[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if ids[v] == -1:  
                    dfs(v, u)
                    if low[v] < low[u]:
                        low[u] = low[v]
                    if low[v] > ids[u]:
                        critical.append([u, v])
                else:
                    if ids[v] < low[u]:
                        low[u] = ids[v]
        dfs(0, -1)
        return critical
