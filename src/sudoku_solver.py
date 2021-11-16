from .reader import Reader
from .puzzle import Puzzle

class SudokuSolver:

    def __init__(this):
        this.puzzle = Puzzle()

    def read_from_file(this, path):
        reader = Reader()
        this.puzzle = reader.read_from_file(path)
        this.initial_state = reader.read_from_file(path)

    def print_to_console(this):
        this.puzzle.print_to_console()
        
    def validate_puzzle(this):

        for i in range(0,9):
            if not this.puzzle.validate_column(i):
                print(F"Invalid Column at {i}")
                return
            if not this.puzzle.validate_row(i):
                print(F"Invalid Row at {i}")
                return
            if not this.puzzle.validate_square(i):
                print(F"Invalid Square at {i}")
                return
        
        print("Puzzle is valid")


    
                
                
