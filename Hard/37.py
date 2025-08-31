class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        cols = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        boxes = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[(int(i / 3) * 3) + int(j / 3)].remove(val)
        
        def backtrack(i, j, board):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    return True
                if j < 8:
                    return backtrack(i, j + 1, board)
                elif i < 8 and j == 8:
                    return backtrack(i + 1, 0, board)
            hash_set = rows[i] & cols[j] & boxes[(i // 3) * 3 + j // 3]
            for s in hash_set:
                board[i][j] = str(s)
                rows[i].remove(s)
                cols[j].remove(s)
                boxes[(int(i / 3) * 3) + int(j / 3)].remove(s)

                if (i == 8 and j == 8) or (j < 8 and backtrack(i, j + 1, board)) or (i < 8 and j == 8 and backtrack(i + 1, 0, board)):
                    return True
                board[i][j] = '.'
                rows[i].add(s)
                cols[j].add(s)
                boxes[(int(i / 3) * 3) + int(j / 3)].add(s)
        backtrack(0, 0, board)
      
