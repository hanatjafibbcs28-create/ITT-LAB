class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r in range(m):
            if r not in zero_rows: 
                for c in zero_cols:
                    matrix[r][c] = 0
        zero_template = [0] * n
        for r in zero_rows:
            matrix[r][:] = zero_template
