from .sudoku_solver import SudokuSolver
from .puzzle import Puzzle


class BruteForceSolver(SudokuSolver):

    def __init__(this):
        super().__init__()

    def solve(this):
        '''
            Kicks off the DFS algorithm
        '''
        start_x, start_y = this.puzzle.get_next_index(0, 0)

        return this.depth_first_alogrithm(start_x, start_y)


    def depth_first_alogrithm(this, x:int, y:int):
        '''
            The DFS algorithm will brute force the puzzle, checking each possible value for each empty index.
            If the algorithm reaches a valid endstate, True is returned. 
        '''

        #Iterate untill a feasible endstate has been found
        for i in range(1,10):
            this.puzzle.set_value(x,y,i)

            #If the newly inserted value is valid
            if this.puzzle.validate_row(y) and this.puzzle.validate_column(x) and this.puzzle.validate_square(x, y):

                next_x, next_y = this.puzzle.get_next_index(x,y)

                #If there are no more empty indices, return True, as the algorithm is done.
                if next_x == -1 or next_y == -1:
                    return True
                
                #If the recursion returns True, propagate this back up.
                if this.depth_first_alogrithm(next_x, next_y):
                    return True

        #If no feasible endstate is found, we return False to propagate this back up
        this.puzzle.set_value(x,y,0)
        return False
