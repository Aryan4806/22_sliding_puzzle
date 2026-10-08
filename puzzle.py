import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        # Start with the solved board
        board = list(range(1, self.size * self.size)) + [0]

        # Position of the blank tile
        blank = len(board) - 1

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Avoid immediately undoing the previous move
        previous_blank = None

        # Scramble using only legal blank-tile moves
        for _ in range(200):
            row = blank // self.size
            col = blank % self.size

            valid_moves = []

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < self.size and 0 <= new_col < self.size:
                    new_blank = new_row * self.size + new_col

                    if new_blank != previous_blank:
                        valid_moves.append(new_blank)

            # If avoiding the previous move leaves no options,
            # allow all legal moves.
            if not valid_moves:
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if 0 <= new_row < self.size and 0 <= new_col < self.size:
                        valid_moves.append(new_row * self.size + new_col)

            new_blank = random.choice(valid_moves)

            # Swap the blank with the neighboring tile
            board[blank], board[new_blank] = board[new_blank], board[blank]

            previous_blank = blank
            blank = new_blank

        return [
            board[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        r, c = self.blank_pos()
        dr, dc = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}[direction]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False
        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
        return True

    def solved(self):
        return sum(self.board, []) == list(range(1, self.size * self.size)) + [0]
