class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row = [False] * m  # Step 1: Initialize row marker
        col = [False] * n  # Step 1: Initialize column marker

        # Step 2: Mark rows and columns where 0 is found
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        # Step 3: Zero out rows
        for i in range(m):
            if row[i]:
                for j in range(n):
                    matrix[i][j] = 0

        # Step 4: Zero out columns
        for j in range(n):
            if col[j]:
                for i in range(m):
                    matrix[i][j] = 0
