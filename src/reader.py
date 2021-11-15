
from .puzzle import Puzzle

class Reader:
    
    def read_from_file(this, path):
        '''
            Reads a puzzle from a txt file.
        '''
        puzzle = Puzzle()

        file = open(path, "r")
        lines = file.readlines()
        puzzle.parse_from_lines(lines)


        file.close()
        return puzzle