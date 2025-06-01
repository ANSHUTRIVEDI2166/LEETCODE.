from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)

        def get_board_pos(square):
            row = (square - 1) // n
            col = (square - 1) % n
            r = n - 1 - row
            c = col if row % 2 == 0 else n - 1 - col
            return r, c

        visited = set()
        queue = deque([(1, 0)])  # (current square, number of moves)

        while queue:
            square, moves = queue.popleft()
            for step in range(1, 7):  # dice roll: 1 to 6
                next_square = square + step
                if next_square > n * n:
                    continue
                r, c = get_board_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1
