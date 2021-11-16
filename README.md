# SudokuSolver

This package contains a simple sudoku solver. At this moment, the only method for solving a puzzle is through brute force.

# Usage

Simply include the package and instantiate a solver like so:

```
from sudoku_solver.brute_force_solver import BruteForceSolver

solver = BruteForceSolver()
solver.read_from_file(file_name)

if solver.solve():
    solved_puzzle = solver.get_puzzle()
```