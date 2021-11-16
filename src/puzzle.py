

class Puzzle:

    def __init__(this):
        this.board = this._generate_empty_board()

        #Fitness is used in some of the algorithms.
        #We use a low value as high fitness
        this.fitness = 9999

    
    def set_value(this, x:int, y:int, value):
        this.board[y][x] = value

    def index(this, x:int, y:int):
        '''
            Returns value at index
        '''
        return this.board[y][x]

    def set_fitness(this, fitness:int):
        this.fitness = fitness

    def get_fitness(this):
        return this.fitness


    def validate_field(this, x:int, y:int):
        '''
            Checks all three constraints for a given field.
        '''

        #This notation is used, so that if a validation fails, we can immediately return false without having
        #to execute the other evaluations.
        if not this.validate_square(x, y) or not this.validate_column(x) or not this.validate_row(y):
            return False


    def validate_square(this, x:int, y:int):
        '''
            Returns true if a square is valid
        '''

        #Get x and y value of topleft index of the 3x3 square
        square_x = x - (x % 3)
        square_y = y - (y % 3)
        elements = []

        for i in range(square_x, square_x + 3):
            for j in range(square_y, square_y + 3):
                field = this.index(i,j)
                if field != 0:
                    elements.append(field)

        return this._validate_list(elements)

    def validate_row(this, y:int):
        '''
            Returns true if a row is valid
        '''

        row = this.board[y]
        return this._validate_list(row)
        

    def validate_column(this, x:int):
        '''
            Returns true if a column is valid
        '''
        column = list(map(lambda el: el[x], this.board))
        return this._validate_list(column)

    def get_next_index(this, x:int, y:int):
        '''
            Returns the next index, going from left to right and top to bottom.
            Will only return indices with empty values.
        '''

        while y < 9:
            while x < 9:
                if this.index(x,y) == 0:
                    return x, y
                x += 1
            x = 0
            y += 1
        return -1, -1
                

    def _validate_list(this, elements:[]):
        '''
            Validates a list of elements
        '''
        #Filter empty spaces
        filtered = list(filter(lambda x: x != 0, elements))
        
        #check for duplicates
        return len(filtered) == len(set(filtered))

    
    def parse_from_lines(this, lines: []):
        '''
            The file reader will open a file and retrieve the individual lines of text.
            These lines are parsed into the board object in this function.
        '''

        for i in range(0,9):
            for j in range(0,9):
                this.board[i][j] = int(lines[i][j])

    def _generate_empty_board(this):
        '''
            A board contains 9 columns and 9 rows.
            For easy querying, we will use a list of lists.
            An empty field will have value 0.
        '''

        board = []

        for i in range(0,9):
            board.append([])
            for j in range(0,9):
                board[i].append(0)
        
        return board



    def print_to_console(this):
        
        for i in range(0,9):
            line = ""
            for j in range(0,9):
                line = line + str(this.board[i][j])
            print(line)

            