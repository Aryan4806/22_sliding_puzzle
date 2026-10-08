import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = 4
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))

        if hasattr(self, "finished"):
            elapsed = int(self.finished - self.started)
        else:
            elapsed = int(time.monotonic() - self.started)

        print("Moves:", self.moves, " Time:", elapsed, "s")

    def run(self):
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")

        while True:
            self.display()

            key = input("> ").strip().lower()

            if key == "q":
                return

            if key not in "wasd":
                print("Use W/A/S/D.")
                continue

            if self.puzzle.move(key):
                self.moves += 1

                if self.puzzle.solved():
                    self.finished = time.monotonic()
                    self.display()
                    print("Puzzle solved! Congratulations!")
                    return
            else:
                print("That move is not possible.")