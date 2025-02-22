import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        rows = 10
        cols = 12
        maze1 = Maze(2, 2, rows, cols, 10, 10)
        self.assertEqual(
            len(maze1._cells),
            cols,
        )
        self.assertEqual(
            len(maze1._cells[0]),
            rows,
        )
        self.assertEqual(
            maze1._cells[0][0].top_wall,
            False
        )
        self.assertEqual(
            maze1._cells[maze1._num_cols - 1][maze1._num_rows - 1].bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()