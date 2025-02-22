from window import Window
from shapes import *
from cell import Cell
from maze import *

CELL_SIZE = (50, 50)

def main():
    print("opening window")
    win = Window(800, 600)

    maze = Maze(2, 2, 4, 4, CELL_SIZE[0], CELL_SIZE[1], win, 10)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()