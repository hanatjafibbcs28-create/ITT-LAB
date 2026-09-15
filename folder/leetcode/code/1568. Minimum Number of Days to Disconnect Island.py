class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def count_islands() -> int:
            visited = [[False] * n for _ in range(m)]
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        queue = [(i, j)]
                        visited[i][j] = True
                        head = 0
                        while head < len(queue):
                            r, c = queue[head]
                            head += 1
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    queue.append((nr, nc))
            return islands
        if count_islands() != 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        return 2
