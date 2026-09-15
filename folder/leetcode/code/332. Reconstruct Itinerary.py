class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = {}
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse=True)
        route = []
        stack = ["JFK"]
        while stack:
            curr = stack[-1]
            if curr in graph and graph[curr]:
                stack.append(graph[curr].pop())
            else:
                route.append(stack.pop())
        return route[::-1]
