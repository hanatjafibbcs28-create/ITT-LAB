class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m * n:
            return False
        from collections import Counter
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
        if board_counts[word[-1]] < board_counts[word[0]]:
            word = word[::-1]
        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            found = (dfs(r + 1, c, i + 1) or 
                     dfs(r - 1, c, i + 1) or 
                     dfs(r, c + 1, i + 1) or 
                     dfs(r, c - 1, i + 1))
            board[r][c] = temp
            return found
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True           
        return False
