from .sudoku_solver import SudokuSolver
from .puzzle import Puzzle
import random

class GeneticAlgorithmSolver(SudokuSolver):
    '''
        A genetic algorithm has several components:
        - A fitness function to determine fitness of current state
        - A representation of a state to a genome
        - A method for combining states
        - A method for mutating state

        DO NOT USE!! This algorithm is far to slow!!
    '''

    def __init__(this):
        super().__init__()
        this.pool_size = 5000
        this.max_iterations = 100000
        this.mutations = 2

    def solve(this):
        '''
            Execute the genetic algorithm.
            If the algorithm succeeds, the state will be set as a property.
            If the algorithm fails, we return False.
        '''

        #We set a range of mutable indices.
        #We can deterministically pick from these indices during mutations.
        this.mutable_indices = []
        
        for i in range(0, 9):
            for j in range(0, 9):
                if this.initial_state.index(i, j) == 0:
                    this.mutable_indices.append([i,j])

        puzzle = this.initial_state
        this.initial_state = puzzle
        states = this._generate_states(this.pool_size)

        for i in range(0, this.max_iterations):

            #Determine fitness for each state
            for j in range(0, this.pool_size):
                fitness = this._determine_fitness_simple(states[j])
                #fitness = this._determine_fitness_simple(states[j])

                #If we have found a result, return it
                if fitness == 0:
                    this.puzzle = states[j]
                    return True

                states[j].set_fitness(fitness)
            
            #Sort the list of states, from highest fitness to lowest (high value for fitness = low fitness)
            states.sort(key=lambda x: x.fitness, reverse=False)

            if i % 100 == 0:
                aver = sum(list(map(lambda x: x.get_fitness(), states))) / this.pool_size
                print(f"Iteration: {i}, best solution: {states[0].get_fitness()}, avg: {aver}")


            new_states = []
            #Take only the fittest half of the states
            #Now we generate a new set of states
            for j in range(0, int(this.pool_size / 2)):
                new_state1 = this._combine_states(states[j], states[j + 1])
                new_state2 = this._combine_states(states[j], states[j + 2])
                new_states.append(new_state1)
                new_states.append(new_state2)

            #A small mutation is performed for each state
            #We mutate twice (mutate a single field)
            for j in range(0, this.pool_size):
                new_states[j] = this._mutate_small(new_states[j])

            states = new_states
        return False


    def _determine_fitness_per_point(this, puzzle: Puzzle):
        '''
            Determines the fitness of a state.
            To keep it simple, the number of incorrect entries is the fitness. (optimal fitness = 0)
        '''

        fitness = 0

        for i in range(0,9):
            for j in range(0,9):
                fitness = fitness +  (not puzzle.validate_square(i, j)) + (not puzzle.validate_column(i)) + (not puzzle.validate_row(j))

        return fitness

    def _determine_fitness_simple(this, puzzle: Puzzle):
        '''
        '''

        fitness = 0

        #Fitness of rows
        for i in range(0, 9):
            fitness += 9 - len(set(puzzle.board[i])) #We want to have 9 distinct values, this will result in row fitness 0
        
        #Fitness of columns
        for i in range(0, 9):
            column = list(map(lambda el: el[i], puzzle.board))
            fitness += 9 - len(set(column))
        
        for i in range(0, 3):
            for j in range(0, 3):
                elements = []

                for n in range(i, i + 3):
                    for m in range(j, j + 3):
                        elements.append(puzzle.index(n,m))
                fitness += 9 - len(set(elements))

        return fitness


    
    def _combine_states(this, puzzle1: Puzzle, puzzle2: Puzzle):
        '''
            Combines two states (genomes) into a new state.
            We will simply take some rows from the left, and some from the right.
        '''

        combined_puzzle = Puzzle()

        for i in range(0, 9):
            combined_puzzle.board[i] = puzzle1.board[i][:] if i % 2 ==0 else puzzle2.board[i][:]

        return combined_puzzle

    
    def _mutate_small(this, puzzle: Puzzle):
        '''
            Performs a small mutation to the state. We set one index randomly.
        '''

        #Get two indices and set them to a random value.
        #These indices must not be set in the initial state.

        coord = this.mutable_indices[random.randint(0, len(this.mutable_indices) - 1)]
        puzzle.set_value(coord[0], coord[1], random.randint(1,9))
        coord = this.mutable_indices[random.randint(0, len(this.mutable_indices) - 1)]
        puzzle.set_value(coord[0], coord[1], random.randint(1,9))
        coord = this.mutable_indices[random.randint(0, len(this.mutable_indices) - 1)]
        puzzle.set_value(coord[0], coord[1], random.randint(1,9))

        

        return puzzle

    
    def _generate_states(this, number_of_puzzles):
        '''
            Generates a set of random states based on the initial puzzle.
        '''

        states = []

        for i in range(0, number_of_puzzles):
            states.append(this._generate_state(this.initial_state))

        return states


    def _generate_state(this, initial_state:Puzzle):
        '''
            Generates a single state based on the initial state.
            The state will have random values.
        '''

        puzzle = Puzzle()

        for i in range(0, 9):
            for j in range(0, 9):
                new_value = random.randint(1, 9) if initial_state.index(i, j) == 0 else initial_state.index(i, j) 
                puzzle.set_value(i, j, new_value)

        return puzzle







    