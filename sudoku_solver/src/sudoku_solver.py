from .reader import Reader
from .puzzle import Puzzle

class SudokuSolver:

    def __init__(this):
        this.puzzle = Puzzle()

    def read_from_file(this, path):
        '''
            Read a puzzle from a file
        '''
        reader = Reader()
        this.puzzle = reader.read_from_file(path)
        this.initial_state = reader.read_from_file(path)

    def read_from_lines(this, lines):

        this.puzzle = Puzzle()
        this.initial_state = Puzzle()
        this.puzzle.parse_from_lines(lines)
        this.initial_state.parse_from_lines(lines)
        
    def validate_puzzle(this):
        '''
            Will check each row, col and square to see if the puzzle is valid.
        '''
        for i in range(0,9):
            if not this.puzzle.validate_column(i):
                return False
            if not this.puzzle.validate_row(i):
                return False

        for i in range(0, 3):
            for j in range(0,3):
                if not this.puzzle.validate_square(i*3, j*3):
                    return False

    def get_puzzle(this):
        '''
            Will return a puzzle in list of lists format.
        '''

        return this.puzzle.board



    
                
                
